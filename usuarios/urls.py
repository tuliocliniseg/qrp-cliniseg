from django.urls import path
from .views import (
    login_view,
    logout_view,
    cadastro_view,
    editar_perfil_view,
    alterar_senha_view,
    gerenciar_usuarios_view,
    editar_usuario_view,
    excluir_usuario_view,
    logs_usuarios_view,
)

app_name = "usuarios"  # Define namespace para URLs deste app

urlpatterns = [
    # 🔐 Autenticação
    path('', login_view, name='login_redirect'),  # Redireciona '/' para /login/
    path('login/', login_view, name='login'),    # Página de login
    path('logout/', logout_view, name='logout'), # Logout do sistema

    # 👤 Perfil e conta do usuário
    path('cadastro/', cadastro_view, name='cadastro'),                 # Cadastro de novos usuários
    path('editar-perfil/', editar_perfil_view, name='editar_perfil'),  # Editar perfil
    path('alterar-senha/', alterar_senha_view, name='alterar_senha'),  # Alterar senha

    # 👥 Administração de usuários (para superusuários)
    path('gerenciar/', gerenciar_usuarios_view, name='gerenciar_usuarios'),             # Listar usuários
    path('editar/<int:user_id>/', editar_usuario_view, name='editar_usuario'),          # Editar usuário específico
    path('excluir/<int:user_id>/', excluir_usuario_view, name='excluir_usuario'),       # Excluir usuário específico

    # 📜 Logs de ações dos usuários (para superusuários)
    path('logs/', logs_usuarios_view, name='logs_usuarios'),                           # Visualizar logs
]
