from django.urls import path
from . import views
from relatorios.views import relatorios_gerenciais  # Importa a view de relatórios do app relatorios

app_name = "painel"

urlpatterns = [
    path('perguntas/', views.listar_perguntas, name='listar_perguntas'),
    path('perguntas/editar/<int:pergunta_id>/', views.editar_pergunta, name='editar_pergunta'),
    path('fatores/', views.listar_fatores, name='listar_fatores'),
    path('fatores/editar/<int:fator_id>/', views.editar_fator_acao, name='editar_fator_acao'),
    path('acoes/editar/<int:acao_id>/', views.editar_acao, name='editar_acao'),
    path('logs/', views.logs_usuarios_view, name='logs_usuarios'),

    # ✅ NOVA ROTA: Edição dos textos do diagnóstico
    path('editar-texto-diagnostico/', views.editar_texto_diagnostico, name='editar_texto_diagnostico'),

    # Rota padrão do painel
    path('', views.painel_view, name='painel'),

    # Rota com aba dinâmica do painel
    path('<str:aba>/', views.painel_view, name='painel_aba'),

    path('relatorios/', relatorios_gerenciais, name='relatorios_gerenciais'),
]
