from fpdf import FPDF
from io import BytesIO
import pandas as pd

from painel.models import Fator, Acao, TextoDiagnostico  # Certifique-se que TextoDiagnostico existe

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
    return texto.encode('latin-1', 'replace').decode('latin-1')

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
    setores = [limpar_texto(setor.nome_setor) for setor in empresa.setores.all()]
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
        pdf.cell(0, 10, limpar_texto("Diagnóstico por Fator de Risco Psicossocial"), ln=True, align="C")
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
        pdf.cell(col_widths[0], 8, limpar_texto("Nº"), 1, align='C')
        pdf.cell(col_widths[1], 8, limpar_texto("Fator de Risco"), 1)
        pdf.cell(col_widths[2], 8, limpar_texto("Pontuação"), 1, align='C')
        pdf.cell(col_widths[3], 8, limpar_texto("Classificação"), 1, align='C')
        pdf.cell(col_widths[4], 8, limpar_texto("Ação Recomendada"), 1)
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
    pdf_data = pdf.output(dest='S').encode('latin-1')
    buffer.write(pdf_data)
    buffer.seek(0)
    return buffer


# 📄 Gera o relatório diagnóstico textual com fatores elevados e críticos
def gerar_pdf_diagnostico_empresa(df, empresa):
    pdf = FPDF()
    pdf.add_page()

    # 🔵 Cabeçalho
    pdf.set_font("Arial", "B", 14)
    pdf.image("static/logo_cliniseg.png", x=10, y=8, w=33)
    pdf.cell(0, 10, limpar_texto("Diagnóstico Riscos Psicossociais"), ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, limpar_texto("CLINISEG Medicina e Segurança do Trabalho"), ln=True, align="C")
    pdf.ln(10)

    # ✅ BUSCA DO TEXTO INICIAL SALVO NO BANCO
    try:
        texto_config = TextoDiagnostico.objects.first()
        texto_inicial = limpar_texto(texto_config.texto_inicial.strip()) if texto_config and texto_config.texto_inicial else ""
        texto_final = limpar_texto(texto_config.texto_final.strip()) if texto_config and texto_config.texto_final else ""
    except:
        texto_inicial = ""
        texto_final = ""

    if texto_inicial:
        pdf.set_font("Arial", "", 11)
        for linha in texto_inicial.split("\n"):
            pdf.multi_cell(0, 8, limpar_texto(linha))
        pdf.ln(5)

    # 🔵 Diagnóstico por setor
    for setor, grupo in df.groupby("Setor"):
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, limpar_texto(f"Setor: {setor}"), ln=True)
        num_func = grupo["Funcionários"].iloc[0]
        num_resp = grupo["Respostas"].iloc[0]
        pdf.set_font("Arial", "", 11)
        pdf.cell(0, 8, limpar_texto(f"Nº funcionários: {num_func}"), ln=True)
        pdf.cell(0, 8, limpar_texto(f"Nº respostas válidas: {num_resp}"), ln=True)
        pdf.ln(4)

        for index, linha in grupo.iterrows():
            fator = limpar_texto(linha["Fator"])
            classificacao = limpar_texto(linha["Classificacao"])
            afirmativas = limpar_texto(linha["Afirmativas"])

            pdf.set_font("Arial", "B", 11)
            pdf.multi_cell(0, 8, f"Fator: {fator} - Classificação: {classificacao}")

            pdf.set_font("Arial", "", 11)
            pdf.multi_cell(0, 8, limpar_texto("Afirmativas associadas:"))
            for afirmativa in afirmativas.split("\n"):
                pdf.multi_cell(0, 8, limpar_texto(f"- {afirmativa.strip()}"))
            pdf.ln(3)

    # ✅ TEXTO FINAL DO DIAGNÓSTICO
    if texto_final:
        pdf.set_font("Arial", "", 11)
        pdf.ln(5)
        for linha in texto_final.split("\n"):
            pdf.multi_cell(0, 8, limpar_texto(linha))

    buffer = BytesIO()
    pdf_data = pdf.output(dest='S').encode('latin-1')
    buffer.write(pdf_data)
    buffer.seek(0)
    return buffer
