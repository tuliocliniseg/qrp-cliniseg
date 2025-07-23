from fpdf import FPDF
from io import BytesIO
import pandas as pd

from painel.models import Fator, Acao  # Modelos do banco

# 🧹 Limpeza de texto para garantir compatibilidade com FPDF e remover caracteres incompatíveis
def limpar_texto(texto):
    if not isinstance(texto, str):
        texto = str(texto)
    texto = (
        texto.replace("–", "-")
             .replace("—", "-")   # substitui travessão longo por hífen simples
             .replace("“", '"')
             .replace("”", '"')
             .replace("’", "'")
             .replace("‘", "'")
             .replace("…", "...")
    )
    # REMOVIDO o encode('latin-1', 'ignore').decode('latin-1') para preservar UTF-8
    return texto

# 📊 Classificação personalizada com base na quantidade de perguntas
def classificar_risco_personalizado(pontuacao, num_perguntas):
    if num_perguntas == 1:
        if 4.00 <= pontuacao <= 5.00: return "Baixo"
        elif 3.00 <= pontuacao <= 3.99: return "Moderado"
        elif 2.00 <= pontuacao <= 2.99: return "Elevado"
        elif 1.00 <= pontuacao <= 1.99: return "Crítico"
    elif num_perguntas == 2:
        if 8.00 <= pontuacao <= 10.00: return "Baixo"
        elif 6.00 <= pontuacao <= 7.99: return "Moderado"
        elif 4.00 <= pontuacao <= 5.99: return "Elevado"
        elif 2.00 <= pontuacao <= 3.99: return "Crítico"
    elif num_perguntas == 3:
        if 12.00 <= pontuacao <= 15.00: return "Baixo"
        elif 9.00 <= pontuacao <= 11.99: return "Moderado"
        elif 6.00 <= pontuacao <= 8.99: return "Elevado"
        elif 3.00 <= pontuacao <= 5.99: return "Crítico"
    return ""

# 📄 Gera o relatório por fator para cada setor
def gerar_pdf_fator_risco(df, empresa):
    setores = [setor.nome_setor for setor in empresa.setores.all()]
    fatores = Fator.objects.all().order_by('ordem')

    pdf = FPDF(orientation='L')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_title(limpar_texto(f"Relatório Psicossocial - {empresa.nome}"))

    cores_classificacao = {
        "Baixo": (0, 176, 80),
        "Moderado": (255, 192, 0),
        "Elevado": (255, 102, 0),
        "Crítico": (255, 0, 0),
        "": (255, 255, 255),
    }

    for setor in setores:
        setor_df = df[df["setor"] == setor]
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, limpar_texto(f"Empresa: {empresa.nome}"), ln=True, align="C")
        pdf.cell(0, 10, limpar_texto(f"Setor: {setor}"), ln=True, align="C")
        pdf.ln(5)

        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Diagnóstico por Fator de Risco Psicossocial", ln=True, align="C")
        pdf.ln(4)

        resultados = []
        for fator in fatores:
            perguntas = [p.numero for p in fator.perguntas.all()]
            num_perguntas = len(perguntas)
            colunas = [f"q{num}" for num in perguntas]
            colunas_existentes = [c for c in colunas if c in setor_df.columns]

            if not colunas_existentes or setor_df.empty:
                pontuacao_final = 0
            else:
                respostas = setor_df[colunas_existentes].dropna()
                if respostas.empty:
                    pontuacao_final = 0
                else:
                    medias_colaboradores = respostas.mean(axis=1)
                    pontuacao_final = medias_colaboradores.mean() * num_perguntas

            classificacao = classificar_risco_personalizado(pontuacao_final, num_perguntas)
            acao_obj = Acao.objects.filter(fator=fator, classificacao=classificacao).first()
            acao_texto = acao_obj.descricao if acao_obj else ""
            max_pontuacao = 5 * num_perguntas

            resultados.append({
                "n": fator.ordem,
                "nome": limpar_texto(fator.nome),
                "pontuacao": round(pontuacao_final, 2),
                "max_pontuacao": max_pontuacao,
                "classificacao": classificacao,
                "acao": limpar_texto(acao_texto)
            })

        col_widths = [10, 90, 35, 40, 120]
        total_table_width = sum(col_widths)
        page_width = pdf.w - 2 * pdf.l_margin
        x_table_start = (page_width - total_table_width) / 2 + pdf.l_margin

        pdf.set_font("Arial", "B", 11)
        pdf.set_xy(x_table_start, pdf.get_y())
        pdf.cell(col_widths[0], 8, "Nº", 1, align='C')
        pdf.cell(col_widths[1], 8, "Fator de Risco", 1)
        pdf.cell(col_widths[2], 8, "Pontuação", 1, align='C')
        pdf.cell(col_widths[3], 8, "Classificação", 1, align='C')
        pdf.cell(col_widths[4], 8, "Ação Recomendada", 1)
        pdf.ln()

        pdf.set_font("Arial", "", 10)
        line_height = 6

        for r in resultados:
            cor = cores_classificacao.get(r["classificacao"], (255, 255, 255))
            pdf.set_fill_color(*cor)
            pdf.set_text_color(0, 0, 0)

            text = r["acao"]
            n_lines = pdf.multi_cell(col_widths[4], line_height, text, border=0, split_only=True)
            cell_height = line_height * len(n_lines)

            pdf.set_xy(x_table_start, pdf.get_y())
            pontuacao_texto = f"{r['pontuacao']}/{r['max_pontuacao']}"
            pdf.cell(col_widths[0], cell_height, str(r["n"]), border=1, align='C')
            pdf.cell(col_widths[1], cell_height, r["nome"], border=1)
            pdf.cell(col_widths[2], cell_height, pontuacao_texto, border=1, align='C')
            pdf.cell(col_widths[3], cell_height, r["classificacao"], border=1, align='C', fill=True)

            y_pos = pdf.get_y()
            pdf.multi_cell(col_widths[4], line_height, text, border=1)
            pdf.set_xy(x_table_start, y_pos + cell_height)

        pdf.set_text_color(0, 0, 0)

    buffer = BytesIO()
    buffer.write(pdf.output(dest='S').encode('utf-8'))  # Troquei para utf-8 aqui
    buffer.seek(0)
    return buffer


# 📄 Gera o relatório diagnóstico textual com fatores elevados e críticos
def gerar_pdf_diagnostico_empresa(empresa, df):
    if df.empty:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Nenhum dado disponível para esta empresa.", ln=True, align="C")
        buffer = BytesIO()
        buffer.write(pdf.output(dest='S').encode('utf-8'))  # Troquei para utf-8 aqui
        buffer.seek(0)
        return buffer

    setores = df['setor'].unique()
    setor_funcionarios = {s.nome_setor: s.num_funcionarios for s in empresa.setores.all()}
    fatores = Fator.objects.all().order_by('ordem')

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Inserir logo pequeno no canto superior esquerdo (ajustado para proporção correta)
    try:
        pdf.image('static/img/logo_cliniseg.png', x=10, y=8, w=20, h=20)  # Tamanho ajustado 20x20 px
    except RuntimeError:
        pass

    pdf.set_title(f"Diagnóstico Riscos Psicossociais - {empresa.nome}")
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Diagnóstico Riscos Psicossociais", ln=True, align="C")

    # Nome da empresa abaixo do título
    pdf.set_font("Arial", "", 14)
    pdf.cell(0, 10, limpar_texto(empresa.nome), ln=True, align="C")

    pdf.ln(10)

    # INFORMATIVO inicial em negrito somente no título
    pdf.set_font("Arial", "B", 14)
    texto_titulo_informativo = "INFORMATIVO - Acompanhamento do Questionário de Riscos Psicossociais"
    pdf.cell(0, 10, limpar_texto(texto_titulo_informativo), ln=True)

    pdf.set_font("Arial", "", 12)
    texto_informativo = (
        "Referente ao questionário de avaliação psicossocial aplicado aos colaboradores, informamos que o ano de 2025 está sendo conduzido como fase educativa e preparatória, sem exigência imediata de alteração documental por parte das empresas.\n\n"
        "Entretanto, a partir de 2026, os resultados obtidos passarão a impactar diretamente na elaboração e atualização obrigatória do Programa de Gerenciamento de Riscos (PGR).\n\n"
        "Neste momento, nosso foco é apoiar a empresa com orientações técnicas e sugestões de ações voluntárias, com base nos fatores que indicaram nível de risco elevado na percepção dos colaboradores."
    )
    pdf.multi_cell(0, 7, limpar_texto(texto_informativo))
    pdf.ln(10)

    primeiro_setor = True
    for setor in setores:
        setor_df = df[df["setor"] == setor]
        respostas_validas = len(setor_df)
        if respostas_validas == 0:
            continue

        resultados = []
        for fator in fatores:
            perguntas = [p.numero for p in fator.perguntas.all()]
            colunas = [f'q{n}' for n in perguntas if f'q{n}' in setor_df.columns]
            if not colunas:
                continue
            respostas = setor_df[colunas].dropna()
            if respostas.empty:
                continue

            media_individual = respostas.mean(axis=1)

            if callable(getattr(media_individual, "mean", None)):
                pontuacao_final = float(media_individual.mean()) * len(colunas)
            else:
                pontuacao_final = 0

            classificacao = classificar_risco_personalizado(pontuacao_final, len(colunas))

            if classificacao not in ["Elevado", "Crítico"]:
                continue

            acao = Acao.objects.filter(fator=fator, classificacao=classificacao).first()
            resultados.append({
                "fator": fator.nome,
                "classificacao": classificacao,
                "perguntas": [p.texto for p in fator.perguntas.all()],
                "acao": acao.descricao if acao else "",
            })

        if not primeiro_setor:
            pdf.add_page()  # Adiciona página para setores após o primeiro
        else:
            primeiro_setor = False

        pdf.set_font("Arial", "B", 13)
        pdf.cell(0, 10, f"Setor: {setor}", ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 8, f"Nº funcionários: {setor_funcionarios.get(setor, 'N/D')}", ln=True)
        pdf.cell(0, 8, f"Nº respostas válidas: {respostas_validas}", ln=True)
        pdf.ln(5)

        if resultados:
            for item in resultados:
                pdf.set_font("Arial", "B", 12)
                pdf.cell(0, 8, f"Fator: {item['fator']} - Classificação: {item['classificacao']}", ln=True)
                pdf.set_font("Arial", "", 11)
                pdf.multi_cell(0, 7, "Afirmativas associadas:")
                for q in item["perguntas"]:
                    pdf.multi_cell(0, 7, f"- {limpar_texto(q)}")
                pdf.set_font("Arial", "I", 11)
                pdf.set_text_color(0, 0, 139)  # Azul escuro para destacar ação
                pdf.multi_cell(0, 7, f"Ação recomendada: {limpar_texto(item['acao'])}")
                pdf.set_text_color(0, 0, 0)
                pdf.ln(4)
        else:
            pdf.set_font("Arial", "I", 11)
            pdf.multi_cell(0, 7, "⚠️ Nenhum fator elevado ou crítico. Nenhuma ação imediata recomendada.")
            pdf.ln(5)

    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    texto_final = (
        "Ressaltamos que, até 26 de maio de 2026, a inclusão dos fatores psicossociais possui caráter educativo. Assim, a empresa tem a possibilidade de, ciente dos resultados e das medidas cabíveis, implementar ações corretivas desde já.\n\n"
        "Antecipar-se agora demonstra comprometimento com o bem-estar dos colaboradores e favorece a cultura de segurança organizacional.\n\n"
        "Diante das informações enviadas acima em relação aos riscos psicossociais, você concorda que estão de acordo com a realidade atual da empresa e que estes resultados passarão a ser introduzidos no PGR de 2025?\n\n"
        "Dessa forma, um novo levantamento será realizado no próximo ano - quando a inclusão será obrigatória -, e apenas os fatores que ainda estiverem presentes no ambiente de trabalho serão incluídos no PGR.\n\n"
        "Ficamos no aguardo do seu retorno quanto à forma como desejam proceder.\n\n"
        "Colocamo-nos à disposição para auxiliar a empresa em qualquer etapa de análise ou implementação de melhorias."
    )
    pdf.multi_cell(0, 7, limpar_texto(texto_final))

    buffer = BytesIO()
    buffer.write(pdf.output(dest='S').encode('utf-8'))  # Troquei para utf-8 aqui
    buffer.seek(0)
    return buffer
