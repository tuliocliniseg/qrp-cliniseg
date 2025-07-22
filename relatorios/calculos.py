import pandas as pd

# ─── Mapeamento oficial dos 18 fatores (NOMES FIEIS AO QRP CLINISEG – Eixo Final) ────────────────────────────────
fatores_info = {
    1:  {"nome": "Trabalho sem pausas para descanso", "perguntas": [1, 2]},
    2:  {"nome": "Ritmo intenso de trabalho", "perguntas": [3, 4]},
    3:  {"nome": "Variação de turnos", "perguntas": [5]},
    4:  {"nome": "Capacidade insuficiente para as tarefas", "perguntas": [6, 7]},
    5:  {"nome": "Metas rigorosas", "perguntas": [8, 9]},
    6:  {"nome": "Trabalho remunerado por produção", "perguntas": [10]},
    7:  {"nome": "Desequilíbrio trabalho x descanso", "perguntas": [11, 12]},
    8:  {"nome": "Situações de estresse", "perguntas": [13, 14]},
    9:  {"nome": "Sobrecarga mental", "perguntas": [15, 16, 17]},
    10: {"nome": "Exigência cognitiva elevada", "perguntas": [18]},
    11: {"nome": "Comunicação deficiente", "perguntas": [19, 20]},
    12: {"nome": "Conflitos no trabalho", "perguntas": [21, 22]},
    13: {"nome": "Demandas emocionais/afetivas", "perguntas": [23, 24]},
    14: {"nome": "Assédio no trabalho", "perguntas": [25, 26]},
    15: {"nome": "Demandas divergentes", "perguntas": [27, 28]},
    16: {"nome": "Multitarefas com alta carga cognitiva", "perguntas": [29, 30]},
    17: {"nome": "Insatisfação no trabalho", "perguntas": [31, 32, 33]},
    18: {"nome": "Falta de autonomia", "perguntas": [34, 35]},
}

# ─── Classificação por pontuação total ─────────────────────────────────────────────
def classificar_por_pontuacao(pontuacao, num_perguntas):
    if num_perguntas == 1:
        if pontuacao == 5:
            return "Baixo"
        elif pontuacao == 4:
            return "Moderado"
        elif 2 <= pontuacao <= 3:
            return "Elevado"
        elif pontuacao == 1:
            return "Crítico"
    elif num_perguntas == 2:
        if 9 <= pontuacao <= 10:
            return "Baixo"
        elif 7 <= pontuacao <= 8:
            return "Moderado"
        elif 4 <= pontuacao <= 6:
            return "Elevado"
        elif 2 <= pontuacao <= 3:
            return "Crítico"
    elif num_perguntas == 3:
        if 13 <= pontuacao <= 15:
            return "Baixo"
        elif 10 <= pontuacao <= 12:
            return "Moderado"
        elif 6 <= pontuacao <= 9:
            return "Elevado"
        elif 3 <= pontuacao <= 5:
            return "Crítico"
    return "Sem Classificação"

# ─── Ações recomendadas (provisórias, podem ser substituídas) ──────────────────────
def obter_acao_recomendada(fator_id, classificacao):
    acoes_exemplo = {
        (9, "Crítico"): "Realizar intervenção imediata com apoio psicológico e gestão de conflitos.",
        (14, "Elevado"): "Revisar metas e expectativas de produtividade com a liderança.",
        (3, "Moderado"): "Avaliar escalas de turno e rotatividade para mitigar impacto.",
        (17, "Crítico"): "Realizar dinâmicas de grupo e reforçar valores de respeito e empatia.",
    }
    return acoes_exemplo.get((fator_id, classificacao), "")

# ─── Cálculo por fator ─────────────────────────────────────────────────────────────
def calcular_classificacoes_por_fator(df):
    resultados = []

    if df.empty:
        return resultados

    for fator_id, info in fatores_info.items():
        perguntas = info["perguntas"]
        nome = info["nome"]
        num_perguntas = len(perguntas)
        valor_maximo_fator = num_perguntas * 5

        if not all(str(p) in df.columns for p in perguntas):
            continue

        soma_total = df[perguntas].sum().sum()
        num_respostas = len(df)

        media_ponderada = soma_total / (num_respostas * num_perguntas)
        pontuacao_obtida = round(media_ponderada * valor_maximo_fator, 2)

        classificacao = classificar_por_pontuacao(round(pontuacao_obtida), num_perguntas)
        acao = obter_acao_recomendada(fator_id, classificacao) if classificacao in ["Elevado", "Crítico"] else ""

        resultados.append({
            "numero": fator_id,
            "nome": nome,
            "pontuacao_obtida": pontuacao_obtida,
            "pontuacao_maxima": valor_maximo_fator,
            "pontuacao_exibida": f"{pontuacao_obtida} / {valor_maximo_fator}",
            "classificacao": classificacao,
            "acao_recomendada": acao,
        })

    return resultados

# ─── Cálculo consolidado por setor ─────────────────────────────────────────────────
def calcular_consolidado(df):
    if "setor" not in df.columns:
        return []

    setores = []
    for setor_nome in df["setor"].unique():
        df_setor = df[df["setor"] == setor_nome]
        fatores = calcular_classificacoes_por_fator(df_setor)
        setores.append({
            "nome": setor_nome,
            "fatores": fatores
        })
    return setores
