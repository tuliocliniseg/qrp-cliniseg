from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # 🔐 Acesso ao painel administrativo padrão do Django
    path('admin/', admin.site.urls),

    # 👤 Rotas relacionadas ao app de usuários (login, autenticação, cadastro, perfil etc.)
    path('login/', include('usuarios.urls')),  # Prefixo /login/ para urls do app usuarios

    # 📊 Rotas do painel principal
    path('painel/', include('painel.urls')),

    # 🏢 Rotas para empresas
    path('empresas/', include('empresas.urls')),

    # 📈 Rotas para relatórios
    path('relatorios/', include('relatorios.urls')),

    # 📝 Rotas públicas do formulário
    path('formulario/', include('formulario.urls')),

    # 🔄 Redirecionamento da raiz do site para a página de login
    path('', lambda request: redirect('/login/')),
]
