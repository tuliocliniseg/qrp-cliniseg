import os
import django

# Configura o ambiente Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qrp_cliniseg.settings")
django.setup()

from painel.models import Fator, Pergunta

# Lista com todas as perguntas na ordem, associando fator e número exato
perguntas = [
    (1,  1, "O meu tempo de descanso é suficiente para manter a disposição e a atenção no trabalho."),
    (2,  1, "As pausas oferecidas (conforme CLT) são adequadas para a minha recuperação física e mental."),
    (3,  2, "O ritmo do meu trabalho me permite manter o bem estar e atenção durante toda a jornada."),
    (4,  2, "Tenho tempo suficiente para realizar minhas tarefas com a qualidade que eu considero ideal."),
    (5,  3, "A variação de turnos (manhã, tarde, noite) se harmoniza com meu bem-estar e o ritmo do meu trabalho."),
    (6,  4, "Recebo instruções e treinamentos adequados para me sentir seguro e preparado para as minhas atividades."),
    (7,  4, "As capacitações que recebo são adequadas e suficientes para realizar meu trabalho com segurança e qualidade."),
    (8,  5, "Consigo atingir as metas de produtividade com os recursos disponíveis e de forma segura."),
    (9,  5, "As metas de trabalho são realistas e consideram minhas habilidades e capacidade para realizá-las."),
    (10, 6, "A forma como meu salário é definido pela minha produção me traz motivação e conforto."),
    (11, 7, "Consigo equilibrar meu tempo de trabalho com o tempo necessário para meu descanso."),
    (12, 7, "Meu trabalho me permite ter tempo e energia para a vida pessoal e familiar."),
    (13, 8, "Meu trabalho contribui positivamente para meu equilíbrio emocional e bem-estar no dia a dia."),
    (14, 8, "As demandas do meu trabalho são organizadas de forma que consigo manter minha tranquilidade e qualidade de sono."),
    (15, 9, "A quantidade de tarefas que exigem minha atenção e raciocínio são adequadas."),
    (16, 9, "O volume das minhas responsabilidades no trabalho me permite manter meu equilíbrio emocional e me sentir energizado(a)."),
    (17, 9, "Tenho liberdade para errar e aprender com meus enganos, mesmo quando a pressão no trabalho é grande."),
    (18, 10, "Consigo manter o nível de concentração e atenção que meu trabalho exige, sem me sobrecarregar."),
    (19, 11, "As condições do meu ambiente de trabalho (como ruído, isolamento, distância física ou regras rígidas) facilitam a comunicação necessária para realizar minhas tarefas de forma eficaz."),
    (20, 11, "Meu ambiente físico de trabalho facilita a troca de ideias e a interação social com meus colegas."),
    (21, 12, "Percebo que o ambiente de trabalho é tranquilo e livre de conflitos interpessoais."),
    (22, 12, "Sinto que há uma boa colaboração e apoio entre os colegas no meu ambiente de trabalho."),
    (23, 13, "Consigo expressar meus sentimentos de forma autêntica enquanto atendo às exigências da minha função."),
    (24, 13, "As exigências emocionais do trabalho apoiam meu equilíbrio mental, físico e social."),
    (25, 14, "Sinto que o ambiente de trabalho é respeitoso e livre de assédio."),
    (26, 14, "Me sinto seguro(a) para lidar com erros e aprender com eles, sem medo de punições excessivas."),
    (27, 15, "As informações e metas que recebo para a execução do meu trabalho são claras e consistentes, facilitando meu desempenho."),
    (28, 15, "Recebo feedback claro sobre o meu desempenho, que me ajuda a entender como estou “indo” no trabalho."),
    (29, 16, "Consigo gerenciar múltiplas tarefas ao mesmo tempo, mantendo o foco e um bom nível de energia mental."),
    (30, 16, "As tarefas que eu realizo ao mesmo tempo no trabalho favorecem meu bem-estar, contribuindo para meu conforto físico e mental e um bom desempenho."),
    (31, 17, "Estou satisfeito(a) e realizado(a) com as atividades que desempenho no meu trabalho atual."),
    (32, 17, "Meu trabalho e minhas contribuições são reconhecidos e valorizados pela organização."),
    (33, 17, "Sinto-me motivado(a) e engajado(a) para continuar realizando meu trabalho."),
    (34, 18, "Sinto que há espaço para sugerir melhorias e que minhas ideias são consideradas pela empresa."),
    (35, 18, "Meus superiores estão abertos a ouvir minhas preocupações e sugestões no trabalho."),
]

def popular_perguntas():
    print("Iniciando inserção das perguntas...")

    for numero, fator_ordem, texto in perguntas:
        try:
            fator = Fator.objects.get(ordem=fator_ordem)
        except Fator.DoesNotExist:
            print(f"Fator {fator_ordem} não encontrado, pulando pergunta {numero}")
            continue

        pergunta, criada = Pergunta.objects.get_or_create(
            numero=numero,
            defaults={
                'texto': texto,
                'fator': fator,
            }
        )
        if criada:
            print(f"Pergunta {numero} criada: {texto}")
        else:
            print(f"Pergunta {numero} já existe.")

    print("Fim da inserção das perguntas.")

if __name__ == "__main__":
    popular_perguntas()
