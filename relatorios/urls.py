from django.urls import path
from . import views

app_name = 'relatorios'  # <-- essa linha faltava

urlpatterns = [
    # 🔹 Página principal com seleção de empresa e opções de relatórios
    path('', views.relatorios_gerenciais, name='relatorios_gerenciais'),

    # 🔷 Geração do Relatório por Fator de Risco (PDF)
    # Exibe diagnóstico por setor, fator e ações recomendadas
    path('relatorio-fator/<slug:slug>/', views.download_relatorio_fator, name='relatorio_fator'),

    # 🟩 Geração do Diagnóstico Psicossocial (PDF)
    # Exibe texto técnico com fatores elevados e críticos por setor
    path('relatorio-diagnostico/<slug:slug>/', views.download_relatorio_diagnostico, name='relatorio_diagnostico'),
]
