from .acoes_fatores import _DEFAULT_ACOES

# ─────────────────────────────────────────────────────────────────────────────
# 🧠 Mapeamento dos 18 fatores com perguntas e nomes oficiais
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

# ─────────────────────────────────────────────────────────────────────────────
# 📊 Função para classificar o risco psicossocial por pontuação e número de perguntas
def classificar_risco_personalizado(pontuacao, num_perguntas):
    if num_perguntas == 1:
        if pontuacao == 5:
            return "Baixo"
        elif pontuacao == 4:
            return "Moderado"
        elif 2 <= pontuacao <= 3:
            return "Elevado"
        elif pontuacao <= 1:
            return "Crítico"
    elif num_perguntas == 2:
        if 9 <= pontuacao <= 10:
            return "Baixo"
        elif 7 <= pontuacao <= 8:
            return "Moderado"
        elif 4 <= pontuacao <= 6:
            return "Elevado"
        elif pontuacao <= 3:
            return "Crítico"
    elif num_perguntas == 3:
        if 13 <= pontuacao <= 15:
            return "Baixo"
        elif 10 <= pontuacao <= 12:
            return "Moderado"
        elif 6 <= pontuacao <= 9:
            return "Elevado"
        elif pontuacao <= 5:
            return "Crítico"
    return "Sem Classificação"

# ─────────────────────────────────────────────────────────────────────────────
# 🧾 Busca a ação recomendada com base no fator e sua classificação
def obter_acao_recomendada(fator_id, classificacao):
    for acao in _DEFAULT_ACOES:
        if acao["numero"] == fator_id:
            if classificacao == "Baixo":
                return acao["acao_baixo"]
            elif classificacao == "Moderado":
                return acao["acao_moderado"]
            elif classificacao == "Elevado":
                return acao["acao_elevado"]
            elif classificacao == "Crítico":
                return acao["acao_critico"]
    return ""
