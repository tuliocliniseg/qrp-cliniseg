from painel.models import Fator, Pergunta

# Lista oficial dos 18 fatores
fatores_texto = [
    "Trabalho sem pausas para descanso",
    "Ritmo intenso de trabalho",
    "Variação de turnos",
    "Capacidade insuficiente para as tarefas",
    "Metas rigorosas",
    "Trabalho remunerado por produção",
    "Desequilíbrio trabalho x descanso",
    "Situações de estresse",
    "Sobrecarga mental",
    "Exigência cognitiva elevada",
    "Comunicação deficiente",
    "Conflitos no trabalho",
    "Demandas emocionais/afetivas",
    "Assédio no trabalho",
    "Demandas divergentes",
    "Multitarefas com alta carga cognitiva",
    "Insatisfação no trabalho",
    "Falta de autonomia"
]

# Perguntas oficiais (exatamente 35, organizadas por fator)
perguntas_por_fator = {
    "Trabalho sem pausas para descanso": [
        "O meu tempo de descanso é suficiente para manter a disposição e a atenção no trabalho.",
        "As pausas oferecidas (conforme CLT) são adequadas para a minha recuperação física e mental."
    ],
    "Ritmo intenso de trabalho": [
        "O ritmo do meu trabalho me permite manter o bem estar e atenção durante toda a jornada.",
        "Tenho tempo suficiente para realizar minhas tarefas com a qualidade que eu considero ideal."
    ],
    "Variação de turnos": [
        "A variação de turnos (manhã, tarde, noite) se harmoniza com meu bem-estar e o ritmo do meu trabalho."
    ],
    "Capacidade insuficiente para as tarefas": [
        "Recebo instruções e treinamentos adequados para me sentir seguro e preparado para as minhas atividades.",
        "As capacitações que recebo são adequadas e suficientes para realizar meu trabalho com segurança e qualidade."
    ],
    "Metas rigorosas": [
        "Consigo atingir as metas de produtividade com os recursos disponíveis e de forma segura.",
        "As metas de trabalho são realistas e consideram minhas habilidades e capacidade para realizá-las."
    ],
    "Trabalho remunerado por produção": [
        "A forma como meu salário é definido pela minha produção me traz motivação e conforto."
    ],
    "Desequilíbrio trabalho x descanso": [
        "Consigo equilibrar meu tempo de trabalho com o tempo necessário para meu descanso.",
        "Meu trabalho me permite ter tempo e energia para a vida pessoal e familiar."
    ],
    "Situações de estresse": [
        "Meu trabalho contribui positivamente para meu equilíbrio emocional e bem-estar no dia a dia.",
        "As demandas do meu trabalho são organizadas de forma que consigo manter minha tranquilidade e qualidade de sono."
    ],
    "Sobrecarga mental": [
        "A quantidade de tarefas que exigem minha atenção e raciocínio são adequadas.",
        "O volume das minhas responsabilidades no trabalho me permite manter meu equilíbrio emocional e me sentir energizado(a).",
        "Tenho liberdade para errar e aprender com meus enganos, mesmo quando a pressão no trabalho é grande."
    ],
    "Exigência cognitiva elevada": [
        "Consigo manter o nível de concentração e atenção que meu trabalho exige, sem me sobrecarregar."
    ],
    "Comunicação deficiente": [
        "As condições do meu ambiente de trabalho (como ruído, isolamento, distância física ou regras rígidas) facilitam a comunicação necessária para realizar minhas tarefas de forma eficaz.",
        "Meu ambiente físico de trabalho facilita a troca de ideias e a interação social com meus colegas."
    ],
    "Conflitos no trabalho": [
        "Percebo que o ambiente de trabalho é tranquilo e livre de conflitos interpessoais.",
        "Sinto que há uma boa colaboração e apoio entre os colegas no meu ambiente de trabalho."
    ],
    "Demandas emocionais/afetivas": [
        "Consigo expressar meus sentimentos de forma autêntica enquanto atendo às exigências da minha função.",
        "As exigências emocionais do trabalho apoiam meu equilíbrio mental, físico e social."
    ],
    "Assédio no trabalho": [
        "Sinto que o ambiente de trabalho é respeitoso e livre de assédio.",
        "Me sinto seguro(a) para lidar com erros e aprender com eles, sem medo de punições excessivas."
    ],
    "Demandas divergentes": [
        "As informações e metas que recebo para a execução do meu trabalho são claras e consistentes, facilitando meu desempenho.",
        "Recebo feedback claro sobre o meu desempenho, que me ajuda a entender como estou “indo” no trabalho."
    ],
    "Multitarefas com alta carga cognitiva": [
        "Consigo gerenciar múltiplas tarefas ao mesmo tempo, mantendo o foco e um bom nível de energia mental.",
        "As tarefas que eu realizo ao mesmo tempo no trabalho favorecem meu bem-estar, contribuindo para meu conforto físico e mental e um bom desempenho."
    ],
    "Insatisfação no trabalho": [
        "Estou satisfeito(a) e realizado(a) com as atividades que desempenho no meu trabalho atual.",
        "Meu trabalho e minhas contribuições são reconhecidos e valorizados pela organização.",
        "Sinto-me motivado(a) e engajado(a) para continuar realizando meu trabalho."
    ],
    "Falta de autonomia": [
        "Sinto que há espaço para sugerir melhorias e que minhas ideias são consideradas pela empresa.",
        "Meus superiores estão abertos a ouvir minhas preocupações e sugestões no trabalho."
    ],
}

def popular():
    for fator_nome in fatores_texto:
        # Cria ou pega o fator pelo nome
        fator_obj, criado = Fator.objects.get_or_create(nome=fator_nome)
        # Busca as perguntas deste fator na lista
        perguntas = perguntas_por_fator.get(fator_nome, [])
        # Para cada pergunta, cria ou pega existente
        for pergunta_texto in perguntas:
            Pergunta.objects.get_or_create(texto=pergunta_texto, fator=fator_obj)
    print("Fatores e perguntas populados com sucesso!")

# Rodar a função para popular
popular()
