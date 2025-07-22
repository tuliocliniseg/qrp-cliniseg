from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 🔐 Acesso ao painel administrativo padrão do Django
    path('admin/', admin.site.urls),

    # 👤 Rotas do app de usuários (login, autenticação, perfil, etc.)
    path('', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),

    # 📊 Painel administrativo com abas: Início, Dados, Relatórios, Configurações
    path('painel/', include(('painel.urls', 'painel'), namespace='painel')),

    # 🏢 Rotas para empresas, setores e gestão organizacional
    path('empresas/', include(('empresas.urls', 'empresas'), namespace='empresas')),

    # 📈 Geração e download de relatórios PDF
    path('relatorios/', include(('relatorios.urls', 'relatorios'), namespace='relatorios')),

    # 📝 Formulário público de avaliação psicossocial
    path('formulario/', include(('formulario.urls', 'formulario'), namespace='formulario')),

    # 📋 Rotas para submissão e visualização de respostas
    path('respostas/', include(('respostas.urls', 'respostas'), namespace='respostas')),
]
