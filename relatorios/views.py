# ─────────────────────────────────────────────────────────────
# 🔹 Importações necessárias
# ─────────────────────────────────────────────────────────────
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from empresas.models import Empresa
from respostas.models import Resposta
from .services import gerar_pdf_fator_risco, gerar_pdf_diagnostico_empresa
import pandas as pd
import logging

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
        df = pd.DataFrame(list(respostas.values(
            'id',
            'empresa__nome',
            'setor__nome_setor',
            'sexo',
            'faixa_etaria',
            *[f'q{i}' for i in range(1, 36)]
        )))

        df.rename(columns={'setor__nome_setor': 'setor'}, inplace=True)

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
        # Construção segura da lista de dados, evitando ausência de setores
        dados = []
        for resposta in respostas:
            linha = {
                "empresa": resposta.empresa.nome,
                "setor": resposta.setor.nome_setor if resposta.setor else "NÃO INFORMADO",
                "sexo": resposta.sexo,
                "faixa_etaria": resposta.faixa_etaria
            }
            for i in range(1, 36):
                linha[f'q{i}'] = getattr(resposta, f'q{i}', None)
            dados.append(linha)

        df = pd.DataFrame(dados)

        # Validação do DataFrame antes da geração do PDF
        if df.empty or 'setor' not in df.columns:
            return HttpResponse("Erro: dados insuficientes para gerar o diagnóstico.", status=500)

        # Chamada corrigida da função de geração do PDF, enviando DataFrame já preparado
        pdf_bytes = gerar_pdf_diagnostico_empresa(empresa, df)

        response = HttpResponse(pdf_bytes, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="Diagnostico_Riscos_Psicossociais_{slug}.pdf"'
        return response

    except Exception as e:
        logger.error(f"[ERRO] Falha ao gerar diagnóstico psicossocial: {str(e)}")
        return HttpResponse("Erro ao gerar o diagnóstico psicossocial.", status=500)
