from django.urls import path
from . import views

app_name = "empresas"  # Define namespace para URLs do app empresas

urlpatterns = [
    path('cadastrar/', views.cadastrar_empresa, name='cadastrar_empresa'),
    path('listar/', views.listar_empresas, name='listar_empresas'),
    path('editar/<int:empresa_id>/', views.editar_empresa, name='editar_empresa'),
    path('excluir/<int:empresa_id>/', views.excluir_empresa, name='excluir_empresa'),
    path('painel/', views.painel_empresas_view, name='painel_empresas'),
]