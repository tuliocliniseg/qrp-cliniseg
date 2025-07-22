from painel.models import Fator, Acao

def popular_ou_atualizar_acoes_oficiais():
    print("### Iniciando atualização das ações oficiais ###")

    acoes_oficiais = {
        1: {
            "Baixo": "Manter e reforçar as boas práticas de gestão de pausas e descansos.",
            "Moderado": "Avaliar a otimização das pausas e a comunicação sobre sua importância.",
            "Elevado": "Revisar a frequência e duração das pausas, garantindo sua efetividade na recuperação.",
            "Crítico": "Intervenção urgente para garantir o direito a pausas adequadas e o respeito aos limites de jornada."
        },
        2: {
            "Baixo": "Manter um ritmo de trabalho que favoreça o bem-estar e a qualidade das entregas.",
            "Moderado": "Monitorar o ritmo de trabalho e a percepção de tempo para tarefas, buscando otimizações.",
            "Elevado": "Analisar cargas de trabalho e prazos, ajustando-os para evitar sobrecarga e perda de qualidade.",
            "Crítico": "Reavaliar urgentemente o ritmo de trabalho e as expectativas de produtividade, com foco na saúde do trabalhador."
        },
        3: {
            "Baixo": "Manter a organização de turnos e horários que se harmonizam com o bem-estar.",
            "Moderado": "Investigar pontos de ajuste na organização de turnos para melhor harmonia com a vida do trabalhador.",
            "Elevado": "Revisar a política de variação de turnos, considerando seu impacto no bem-estar e ritmo biológico.",
            "Crítico": "Intervenção imediata na gestão de turnos para mitigar impactos severos na saúde e bem-estar."
        },
        4: {
            "Baixo": "Manter e aprimorar os programas de treinamento e capacitação contínuos.",
            "Moderado": "Avaliar a pertinência e suficiência dos treinamentos para novas demandas ou tecnologias.",
            "Elevado": "Reforçar os programas de capacitação e fornecer mais suporte para o desenvolvimento de habilidades.",
            "Crítico": "Revisar urgentemente a matriz de treinamento e o processo de integração, garantindo a qualificação para as tarefas."
        },
        5: {
            "Baixo": "Manter a definição de metas realistas, que consideram recursos e habilidades dos colaboradores.",
            "Moderado": "Realizar acompanhamento individual das metas e condições de trabalho, ajustando quando necessário.",
            "Elevado": "Revisar o processo de definição de metas, garantindo que sejam alcançáveis e seguras, com recursos adequados.",
            "Crítico": "Intervenção imediata na política de metas, considerando redefinição e avaliação dos impactos na saúde."
        },
        6: {
            "Baixo": "Manter a estrutura de remuneração que motive e traga conforto aos colaboradores.",
            "Moderado": "Monitorar a percepção sobre a remuneração por produção, buscando entender eventuais desconfortos.",
            "Elevado": "Avaliar o sistema de remuneração por produção, considerando seus impactos no bem-estar e na pressão.",
            "Crítico": "Análise e redefinição urgentes do sistema de remuneração por produção, se estiver gerando pressão excessiva."
        },
        7: {
            "Baixo": "Promover a cultura de equilíbrio entre vida profissional e pessoal, incentivando o descanso.",
            "Moderado": "Oferecer recursos e flexibilidade para que os colaboradores gerenciem seu tempo e energia.",
            "Elevado": "Revisar as práticas de gestão de jornada e demandas, buscando maior equilíbrio entre trabalho e vida pessoal.",
            "Crítico": "Intervenção imediata para garantir o direito ao tempo de descanso e à vida pessoal, com apoio à desconexão."
        },
        8: {
            "Baixo": "Manter um ambiente de trabalho que promova o equilíbrio emocional e a tranquilidade.",
            "Moderado": "Identificar e gerenciar fontes de estresse potenciais, oferecendo suporte proativo.",
            "Elevado": "Analisar e reestruturar as demandas de trabalho para reduzir o estresse, focando na qualidade de vida.",
            "Crítico": "Intervenção urgente para mitigar fatores de estresse, com apoio psicológico e reavaliação de processos."
        },
        9: {
            "Baixo": "Manter o volume de responsabilidades e a cultura de aprendizado com erros.",
            "Moderado": "Monitorar o volume de trabalho e incentivar a busca por apoio em momentos de pressão.",
            "Elevado": "Revisar a distribuição de tarefas e responsabilidades, garantindo tempo para aprendizado e recuperação.",
            "Crítico": "Intervenção imediata na gestão da carga de trabalho e na cultura de erros, buscando equilíbrio e segurança psicológica."
        },
        10: {
            "Baixo": "Manter a exigência cognitiva em níveis saudáveis, sem sobrecarga.",
            "Moderado": "Avaliar a intensidade da concentração e atenção exigidas, oferecendo estratégias de manejo.",
            "Elevado": "Ajustar as demandas cognitivas e oferecer pausas ativas para evitar a sobrecarga mental.",
            "Crítico": "Reavaliar urgentemente as tarefas que exigem alta carga cognitiva, buscando formas de otimização e revezamento."
        },
        11: {
            "Baixo": "Manter um ambiente que favoreça a comunicação clara e a interação social.",
            "Moderado": "Melhorar canais e ferramentas de comunicação, e estimular momentos de troca social.",
            "Elevado": "Analisar as barreiras à comunicação e interação no ambiente físico, buscando soluções ergonômicas e organizacionais.",
            "Crítico": "Intervenção urgente para remover obstáculos à comunicação eficaz e promover a interação social positiva."
        },
        12: {
            "Baixo": "Manter um ambiente de trabalho colaborativo e livre de conflitos interpessoais.",
            "Moderado": "Promover workshops de comunicação e resolução de conflitos para fortalecer as relações.",
            "Elevado": "Implementar políticas claras de gestão de conflitos e mediação, incentivando a resolução saudável.",
            "Crítico": "Intervenção imediata para endereçar conflitos e restaurar um ambiente de colaboração e respeito mútuo."
        },
        13: {
            "Baixo": "Manter um ambiente onde a expressão autêntica de sentimentos é possível e equilibrada com as exigências.",
            "Moderado": "Oferecer suporte e ferramentas para o manejo das emoções no ambiente de trabalho.",
            "Elevado": "Avaliar as exigências emocionais da função e seus impactos, buscando formas de proteção e apoio.",
            "Crítico": "Intervenção urgente para proteger o bem-estar emocional dos colaboradores, redefinindo expectativas ou oferecendo apoio especializado."
        },
        14: {
            "Baixo": "Manter um ambiente de trabalho respeitoso, seguro e livre de assédio e punições excessivas.",
            "Moderado": "Reforçar a cultura de respeito, os canais de denúncia e as políticas de não assédio.",
            "Elevado": "Implementar ou fortalecer políticas antiassédio, treinamento de lideranças e canais de denúncia confidenciais.",
            "Crítico": "Intervenção imediata e rigorosa para combater assédio, punições indevidas e criar um ambiente de segurança psicológica."
        },
        15: {
            "Baixo": "Manter a clareza e consistência nas informações, metas e feedback sobre o desempenho.",
            "Moderado": "Otimizar os processos de comunicação de metas e o sistema de feedback para maior clareza.",
            "Elevado": "Revisar os processos de comunicação interna e alinhamento de expectativas, garantindo clareza e consistência.",
            "Crítico": "Reestruturar urgentemente os canais de comunicação e as políticas de feedback para eliminar inconsistências."
        },
        16: {
            "Baixo": "Manter a capacidade de gerenciar múltiplas tarefas sem prejuízo ao bem-estar e desempenho.",
            "Moderado": "Oferecer treinamento em gestão de tempo e prioridades para otimizar o multitarefa.",
            "Elevado": "Analisar a necessidade de multitarefas, buscando reduzir a carga cognitiva excessiva e seus impactos.",
            "Crítico": "Intervenção imediata na organização das tarefas e processos para reduzir a sobrecarga cognitiva e proteger o bem-estar."
        },
        17: {
            "Baixo": "Manter e fortalecer o reconhecimento, a valorização e a motivação no trabalho.",
            "Moderado": "Desenvolver programas de reconhecimento e valorização, além de oportunidades de crescimento.",
            "Elevado": "Avaliar os fatores que causam insatisfação, como reconhecimento, valorização e oportunidades de desenvolvimento.",
            "Crítico": "Intervenção imediata para reverter a insatisfação, investindo em reconhecimento, desenvolvimento e engajamento."
        },
        18: {
            "Baixo": "Manter uma cultura que incentive a autonomia e a participação dos colaboradores.",
            "Moderado": "Promover a delegação de responsabilidades e o desenvolvimento de habilidades de liderança.",
            "Elevado": "Revisar os níveis de autonomia e a participação dos colaboradores, buscando maior empoderamento.",
            "Crítico": "Intervenção urgente para aumentar a autonomia dos colaboradores e promover a participação ativa na tomada de decisões."
        },
    }

    for fator_ordem, classificacoes in acoes_oficiais.items():
        print(f"Processando fator {fator_ordem}...")
        try:
            fator = Fator.objects.get(ordem=fator_ordem)
            print(f"Encontrado fator: {fator.nome}")
        except Fator.DoesNotExist:
            print(f"Fator {fator_ordem} não encontrado. Pulando...")
            continue

        for classificacao, descricao in classificacoes.items():
            print(f"  Verificando ação para classificação '{classificacao}'...")

            acoes_existentes = Acao.objects.filter(fator=fator, classificacao=classificacao)
            if acoes_existentes.exists():
                acao = acoes_existentes.first()
                if acao.descricao != descricao:
                    acao.descricao = descricao
                    acao.save()
                    print(f"    Atualizada ação para {classificacao}.")
                else:
                    print(f"    Ação para {classificacao} já está correta.")
                if acoes_existentes.count() > 1:
                    for acao_dup in acoes_existentes[1:]:
                        acao_dup.delete()
                        print(f"    Excluída ação duplicada para {classificacao}.")
            else:
                Acao.objects.create(fator=fator, classificacao=classificacao, descricao=descricao)
                print(f"    Criada ação para {classificacao}.")

    print("### Atualização concluída ###")

if __name__ == "__main__":
    popular_ou_atualizar_acoes_oficiais()
