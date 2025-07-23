# ─────────────────────────────────────────────────────────────
# 🔹 Importações necessárias
# ─────────────────────────────────────────────────────────────
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from empresas.models import Empresa
from respostas.models import Resposta
from .services import gerar_pdf_fator_risco, gerar_pdf_diagnostico_empresa, classificar_risco_personalizado
import pandas as pd
import logging
import traceback

# ─────────────────────────────────────────────────────────────
# 🔸 Logger para debug
# ─────────────────────────────────────────────────────────────
logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────────
# 🔹 View principal que renderiza a página de relatórios
# ─────────────────────────────────────────────────────────────
def relatorios_gerenciais(request):
    empresas = Empresa.objects.all().order_by("nome")
    slug = request.GET.get("empresa_slug") or request.session.get("slug_empresa")
    slug = slug.strip() if slug else None

    empresa = None
    if slug:
        try:
            empresa = Empresa.objects.get(slug=slug)
            request.session["slug_empresa"] = empresa.slug
        except Empresa.DoesNotExist:
            empresa = None

    context = {
        'empresas': empresas,
        'empresa': empresa
    }
    return render(request, 'relatorios/relatorios.html', context)

# ─────────────────────────────────────────────────────────────
# 🔷 View que gera o Relatório por Fator de Risco (PDF)
# ─────────────────────────────────────────────────────────────
def download_relatorio_fator(request, slug):
    empresa = get_object_or_404(Empresa, slug=slug)
    respostas = Resposta.objects.filter(empresa=empresa)

    if not respostas.exists():
        return HttpResponse("Nenhuma resposta disponível para esta empresa.", status=404)

    try:
        # Converte respostas em DataFrame
        df = pd.DataFrame(list(respostas.values(
            'id',
            'empresa__nome',
            'setor__nome_setor',
            'sexo',
            'faixa_etaria',
            *[f'q{i}' for i in range(1, 36)]
        )))
        df.rename(columns={'setor__nome_setor': 'setor'}, inplace=True)

        # Geração do PDF com a função personalizada
        pdf_bytes = gerar_pdf_fator_risco(df, empresa)

        response = HttpResponse(pdf_bytes, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="relatorio_fator_{slug}.pdf"'
        return response

    except Exception as e:
        logger.error(f"[ERRO] Falha ao gerar relatório por fator: {str(e)}")
        return HttpResponse("Erro ao gerar o relatório por fator.", status=500)

# ─────────────────────────────────────────────────────────────
# 🟩 View que gera o Diagnóstico Psicossocial por Empresa (PDF)
# ─────────────────────────────────────────────────────────────
def download_relatorio_diagnostico(request, slug):
    empresa = get_object_or_404(Empresa, slug=slug)
    respostas = Resposta.objects.filter(empresa=empresa)

    if not respostas.exists():
        return HttpResponse("Nenhuma resposta encontrada para esta empresa.", status=404)

    try:
        # --- Passo 1: Converter respostas em DataFrame bruto ---
        dados = []
        for resposta in respostas:
            try:
                setor_nome = resposta.setor.nome_setor if resposta.setor else "NÃO INFORMADO"
                num_funcionarios = resposta.setor.funcionarios if resposta.setor else 0
            except Exception:
                setor_nome = "NÃO INFORMADO"
                num_funcionarios = 0

            linha = {
                "empresa": resposta.empresa.nome,
                "Setor": setor_nome,
                "Funcionários": num_funcionarios,
                "sexo": resposta.sexo,
                "faixa_etaria": resposta.faixa_etaria
            }
            for i in range(1, 36):
                linha[f'q{i}'] = getattr(resposta, f'q{i}', None)
            dados.append(linha)

        df_respostas = pd.DataFrame(dados)

        # --- Passo 2: Preparar agrupamento por setor e fator ---
        from painel.models import Fator  # importe seu modelo de Fator aqui

        fatores = Fator.objects.all().order_by('ordem')
        lista_resultados = []

        for setor_nome, grupo_setor in df_respostas.groupby("Setor"):
            num_funcionarios_setor = grupo_setor["Funcionários"].iloc[0] if not grupo_setor.empty else 0
            num_respostas_setor = len(grupo_setor)

            for fator in fatores:
                perguntas_fator = [f"q{p.numero}" for p in fator.perguntas.all() if f"q{p.numero}" in grupo_setor.columns]
                if not perguntas_fator:
                    continue

                respostas_fator = grupo_setor[perguntas_fator].dropna()
                if respostas_fator.empty:
                    continue

                # Média das respostas por colaborador
                media_colaboradores = respostas_fator.mean(axis=1)
                pontuacao_final = media_colaboradores.mean() * len(perguntas_fator)

                # Classificação conforme função existente (adapte se quiser)
                classificacao = classificar_risco_personalizado(pontuacao_final, len(perguntas_fator))

                # Afirmativas (textos das perguntas)
                afirmativas = "\n".join([p.texto for p in fator.perguntas.all()])

                lista_resultados.append({
                    "Setor": setor_nome,
                    "Funcionários": num_funcionarios_setor,
                    "Respostas": num_respostas_setor,
                    "Fator": fator.nome,
                    "Classificacao": classificacao,
                    "Afirmativas": afirmativas
                })

        # --- Passo 3: Criar DataFrame final para o relatório ---
        df_relatorio = pd.DataFrame(lista_resultados)

        if df_relatorio.empty:
            return HttpResponse("Nenhum dado válido para gerar o diagnóstico.", status=404)

        # --- Passo 4: Gerar PDF com o DataFrame estruturado ---
        pdf_bytes = gerar_pdf_diagnostico_empresa(df_relatorio, empresa)

        response = HttpResponse(pdf_bytes, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="Diagnostico_Riscos_Psicossociais_{slug}.pdf"'
        return response

    except Exception as e:
        logger.error(f"[ERRO] Falha ao gerar diagnóstico psicossocial: {str(e)}\n{traceback.format_exc()}")
        return HttpResponse("Erro ao gerar o diagnóstico psicossocial.", status=500)
