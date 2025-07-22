from django.db import models
from django.conf import settings

# Modelo Fator de Risco Psicossocial
class Fator(models.Model):
    ordem = models.PositiveIntegerField(
        unique=True,
        help_text="Número fixo para ordenar os fatores de 1 a 18"
    )
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    CLASSIFICACAO_CHOICES = [
        ('Baixo', 'Baixo'),
        ('Moderado', 'Moderado'),
        ('Elevado', 'Elevado'),
        ('Crítico', 'Crítico'),
    ]

    classificacao_risco = models.CharField(
        max_length=10,
        choices=CLASSIFICACAO_CHOICES,
        default='Baixo',
        help_text="Classificação do risco deste fator (calculada a partir das respostas)"
    )

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return f"{self.ordem}. {self.nome}"

    # Dicionário com faixas de pontuação e ações recomendadas por fator
    ACOES_POR_FATOR = {
        1: [
            (9, 10, 'Baixo', 'Manter e reforçar as boas práticas de gestão de pausas e descansos.'),
            (7, 8, 'Moderado', 'Avaliar a otimização das pausas e a comunicação sobre sua importância.'),
            (4, 6, 'Elevado', 'Revisar a frequência e duração das pausas, garantindo sua efetividade na recuperação.'),
            (2, 3, 'Crítico', 'Intervenção urgente para garantir o direito a pausas adequadas e o respeito aos limites de jornada.'),
        ],
        2: [
            (9, 10, 'Baixo', 'Manter um ritmo de trabalho que favoreça o bem-estar e a qualidade das entregas.'),
            (7, 8, 'Moderado', 'Monitorar o ritmo de trabalho e a percepção de tempo para tarefas, buscando otimizações.'),
            (4, 6, 'Elevado', 'Analisar cargas de trabalho e prazos, ajustando-os para evitar sobrecarga e perda de qualidade.'),
            (2, 3, 'Crítico', 'Reavaliar urgentemente o ritmo de trabalho e as expectativas de produtividade, com foco na saúde do trabalhador.'),
        ],
        3: [
            (5, 5, 'Baixo', 'Manter a organização de turnos e horários que se harmonizam com o bem-estar.'),
            (4, 4, 'Moderado', 'Investigar pontos de ajuste na organização de turnos para melhor harmonia com a vida do trabalhador.'),
            (2, 3, 'Elevado', 'Revisar a política de variação de turnos, considerando seu impacto no bem-estar e ritmo biológico.'),
            (1, 1, 'Crítico', 'Intervenção imediata na gestão de turnos para mitigar impactos severos na saúde e bem-estar.'),
        ],
        4: [
            (9, 10, 'Baixo', 'Manter e aprimorar os programas de treinamento e capacitação contínuos.'),
            (7, 8, 'Moderado', 'Avaliar a pertinência e suficiência dos treinamentos para novas demandas ou tecnologias.'),
            (4, 6, 'Elevado', 'Reforçar os programas de capacitação e fornecer mais suporte para o desenvolvimento de habilidades.'),
            (2, 3, 'Crítico', 'Revisar urgentemente a matriz de treinamento e o processo de integração, garantindo a qualificação para as tarefas.'),
        ],
        5: [
            (9, 10, 'Baixo', 'Manter a definição de metas realistas, que consideram recursos e habilidades dos colaboradores.'),
            (7, 8, 'Moderado', 'Realizar acompanhamento individual das metas e condições de trabalho, ajustando quando necessário.'),
            (4, 6, 'Elevado', 'Revisar o processo de definição de metas, garantindo que sejam alcançáveis e seguras, com recursos adequados.'),
            (2, 3, 'Crítico', 'Intervenção imediata na política de metas, considerando redefinição e avaliação dos impactos na saúde.'),
        ],
        6: [
            (5, 5, 'Baixo', 'Manter a estrutura de remuneração que motive e traga conforto aos colaboradores.'),
            (4, 4, 'Moderado', 'Monitorar a percepção sobre a remuneração por produção, buscando entender eventuais desconfortos.'),
            (2, 3, 'Elevado', 'Avaliar o sistema de remuneração por produção, considerando seus impactos no bem-estar e na pressão.'),
            (1, 1, 'Crítico', 'Análise e redefinição urgentes do sistema de remuneração por produção, se estiver gerando pressão excessiva.'),
        ],
        7: [
            (9, 10, 'Baixo', 'Promover a cultura de equilíbrio entre vida profissional e pessoal, incentivando o descanso.'),
            (7, 8, 'Moderado', 'Oferecer recursos e flexibilidade para que os colaboradores gerenciem seu tempo e energia.'),
            (4, 6, 'Elevado', 'Revisar as práticas de gestão de jornada e demandas, buscando maior equilíbrio entre trabalho e vida pessoal.'),
            (2, 3, 'Crítico', 'Intervenção imediata para garantir o direito ao tempo de descanso e à vida pessoal, com apoio à desconexão.'),
        ],
        8: [
            (9, 10, 'Baixo', 'Manter um ambiente de trabalho que promova o equilíbrio emocional e a tranquilidade.'),
            (7, 8, 'Moderado', 'Identificar e gerenciar fontes de estresse potenciais, oferecendo suporte proativo.'),
            (4, 6, 'Elevado', 'Analisar e reestruturar as demandas de trabalho para reduzir o estresse, focando na qualidade de vida.'),
            (2, 3, 'Crítico', 'Intervenção urgente para mitigar fatores de estresse, com apoio psicológico e reavaliação de processos.'),
        ],
        9: [
            (13, 15, 'Baixo', 'Manter o volume de responsabilidades e a cultura de aprendizado com erros.'),
            (10, 12, 'Moderado', 'Monitorar o volume de trabalho e incentivar a busca por apoio em momentos de pressão.'),
            (6, 9, 'Elevado', 'Revisar a distribuição de tarefas e responsabilidades, garantindo tempo para aprendizado e recuperação.'),
            (3, 5, 'Crítico', 'Intervenção imediata na gestão da carga de trabalho e na cultura de erros, buscando equilíbrio e segurança psicológica.'),
        ],
        10: [
            (5, 5, 'Baixo', 'Manter a exigência cognitiva em níveis saudáveis, sem sobrecarga.'),
            (4, 4, 'Moderado', 'Avaliar a intensidade da concentração e atenção exigidas, oferecendo estratégias de manejo.'),
            (2, 3, 'Elevado', 'Ajustar as demandas cognitivas e oferecer pausas ativas para evitar a sobrecarga mental.'),
            (1, 1, 'Crítico', 'Reavaliar urgentemente as tarefas que exigem alta carga cognitiva, buscando formas de otimização e revezamento.'),
        ],
        11: [
            (9, 10, 'Baixo', 'Manter um ambiente que favoreça a comunicação clara e a interação social.'),
            (7, 8, 'Moderado', 'Melhorar canais e ferramentas de comunicação, e estimular momentos de troca social.'),
            (4, 6, 'Elevado', 'Analisar as barreiras à comunicação e interação no ambiente físico, buscando soluções ergonômicas e organizacionais.'),
            (2, 3, 'Crítico', 'Intervenção urgente para remover obstáculos à comunicação eficaz e promover a interação social positiva.'),
        ],
        12: [
            (9, 10, 'Baixo', 'Manter um ambiente de trabalho colaborativo e livre de conflitos interpessoais.'),
            (7, 8, 'Moderado', 'Promover workshops de comunicação e resolução de conflitos para fortalecer as relações.'),
            (4, 6, 'Elevado', 'Implementar políticas claras de gestão de conflitos e mediação, incentivando a resolução saudável.'),
            (2, 3, 'Crítico', 'Intervenção imediata para endereçar conflitos e restaurar um ambiente de colaboração e respeito mútuo.'),
        ],
        13: [
            (9, 10, 'Baixo', 'Manter um ambiente onde a expressão autêntica de sentimentos é possível e equilibrada com as exigências.'),
            (7, 8, 'Moderado', 'Oferecer suporte e ferramentas para o manejo das emoções no ambiente de trabalho.'),
            (4, 6, 'Elevado', 'Avaliar as exigências emocionais da função e seus impactos, buscando formas de proteção e apoio.'),
            (2, 3, 'Crítico', 'Intervenção urgente para proteger o bem-estar emocional dos colaboradores, redefinindo expectativas ou oferecendo apoio especializado.'),
        ],
        14: [
            (9, 10, 'Baixo', 'Manter um ambiente de trabalho respeitoso, seguro e livre de assédio e punições excessivas.'),
            (7, 8, 'Moderado', 'Reforçar a cultura de respeito, os canais de denúncia e as políticas de não assédio.'),
            (4, 6, 'Elevado', 'Implementar ou fortalecer políticas antiassédio, treinamento de lideranças e canais de denúncia confidenciais.'),
            (2, 3, 'Crítico', 'Intervenção imediata e rigorosa para combater assédio, punições indevidas e criar um ambiente de segurança psicológica.'),
        ],
        15: [
            (9, 10, 'Baixo', 'Manter a clareza e consistência nas informações, metas e feedback sobre o desempenho.'),
            (7, 8, 'Moderado', 'Otimizar os processos de comunicação de metas e o sistema de feedback para maior clareza.'),
            (4, 6, 'Elevado', 'Revisar os processos de comunicação interna e alinhamento de expectativas, garantindo clareza e consistência.'),
            (2, 3, 'Crítico', 'Reestruturar urgentemente os canais de comunicação e as políticas de feedback para eliminar inconsistências.'),
        ],
        16: [
            (9, 10, 'Baixo', 'Manter a capacidade de gerenciar múltiplas tarefas sem prejuízo ao bem-estar e desempenho.'),
            (7, 8, 'Moderado', 'Oferecer treinamento em gestão de tempo e prioridades para otimizar o multitarefa.'),
            (4, 6, 'Elevado', 'Analisar a necessidade de multitarefas, buscando reduzir a carga cognitiva excessiva e seus impactos.'),
            (2, 3, 'Crítico', 'Intervenção imediata na organização das tarefas e processos para reduzir a sobrecarga cognitiva e proteger o bem-estar.'),
        ],
        17: [
            (13, 15, 'Baixo', 'Manter e fortalecer o reconhecimento, a valorização e a motivação no trabalho.'),
            (10, 12, 'Moderado', 'Desenvolver programas de reconhecimento e valorização, além de oportunidades de crescimento.'),
            (6, 9, 'Elevado', 'Avaliar os fatores que causam insatisfação, como reconhecimento, valorização e oportunidades de desenvolvimento.'),
            (3, 5, 'Crítico', 'Intervenção imediata para reverter a insatisfação, investindo em reconhecimento, desenvolvimento e engajamento.'),
        ],
        18: [
            (9, 10, 'Baixo', 'Manter uma cultura que incentive a autonomia e a participação dos colaboradores.'),
            (7, 8, 'Moderado', 'Promover a delegação de responsabilidades e o desenvolvimento de habilidades de liderança.'),
            (4, 6, 'Elevado', 'Revisar os níveis de autonomia e a participação dos colaboradores, buscando maior empoderamento.'),
            (2, 3, 'Crítico', 'Intervenção urgente para aumentar a autonomia dos colaboradores e promover a participação ativa na tomada de decisões.'),
        ],
    }

    def obter_acao_recomendada(self, pontuacao):
        faixas = self.ACOES_POR_FATOR.get(self.ordem, [])
        for faixa_min, faixa_max, classificacao, acao in faixas:
            if faixa_min <= pontuacao <= faixa_max:
                return classificacao, acao
        return None, None

# Modelo Acao vinculada a um Fator
class Acao(models.Model):
    fator = models.ForeignKey(
        Fator,
        on_delete=models.CASCADE,
        related_name='acoes'
    )
    descricao = models.TextField()
    CLASSIFICACAO_CHOICES = Fator.CLASSIFICACAO_CHOICES
    classificacao = models.CharField(
        max_length=10,
        choices=CLASSIFICACAO_CHOICES,
        default='Baixo',
        help_text="Classificação da ação conforme o risco que ela atende"
    )

    def __str__(self):
        return f"Ação ({self.classificacao}) para {self.fator.nome}"

# Modelo Pergunta vinculada a um Fator
class Pergunta(models.Model):
    numero = models.PositiveIntegerField(
        help_text="Número sequencial da pergunta para ordenar e controlar a sequência"
    )
    texto = models.TextField()
    fator = models.ForeignKey(
        Fator,
        on_delete=models.CASCADE,
        related_name='perguntas'
    )

    class Meta:
        ordering = ['numero']

    def __str__(self):
        return f"{self.numero} - {self.texto[:50]}"

# Modelo para registro de ações no painel (logs)
class LogAcao(models.Model):
    executado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='acoes_executadas_painel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    usuario_alvo = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='acoes_recebidas_painel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    ACAO_CHOICES = [
        ('criar', 'Criar'),
        ('editar', 'Editar'),
        ('excluir', 'Excluir'),
        ('login', 'Login'),
        ('logout', 'Logout'),
    ]
    acao = models.CharField(
        max_length=20,
        choices=ACAO_CHOICES,
        help_text="Tipo de ação executada"
    )
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        alvo = self.usuario_alvo.first_name if self.usuario_alvo else "N/A"
        executor = self.executado_por.first_name if self.executado_por else "N/A"
        data_formatada = self.data_hora.strftime('%d/%m/%Y %H:%M')
        return f"{executor} executou {self.get_acao_display()} em {alvo} em {data_formatada}"
