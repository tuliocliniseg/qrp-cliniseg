from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from .models import LogUsuario

User = get_user_model()  # Usa o modelo de usuário personalizado

# 🔐 Painel principal protegido por login
@login_required
def painel_view(request, aba=None):
    from empresas.models import Empresa, Setor  # Import interno para evitar erro circular
    from django.db.models import Sum

    usuario = request.user
    context = {"usuario": usuario}

    # Se aba não for informada, define 'inicio' como padrão
    if not aba:
        aba = 'inicio'

    if aba == "dados":
        total_empresas = Empresa.objects.count()
        total_setores = Setor.objects.count()
        total_colaboradores = Setor.objects.aggregate(soma=Sum('funcionarios'))['soma'] or 0

        context.update({
            "total_empresas": total_empresas,
            "total_setores": total_setores,
            "total_colaboradores": total_colaboradores,
        })

        return render(request, "painel/dados.html", context)

    elif aba == "inicio":
        return render(request, "painel/inicio.html", context)

    elif aba == "relatorios":
        empresas = Empresa.objects.all().order_by("nome")
        slug = request.GET.get("empresa_slug") or request.session.get("slug_empresa")
        empresa = None
        if slug:
            try:
                empresa = Empresa.objects.get(slug=slug)
                request.session["slug_empresa"] = empresa.slug
            except Empresa.DoesNotExist:
                empresa = None

        context.update({
            "empresas": empresas,
            "empresa": empresa,
        })

        return render(request, "painel/relatorios.html", context)

    elif aba == "configuracoes":
        return render(request, "painel/configuracoes.html", context)

    else:
        return render(request, "painel/inicio.html", context)

# 🔓 Tela de login
def login_view(request):
    if request.user.is_authenticated:
        # Corrigido: usar nome correto da rota com parâmetro
        return redirect('painel:painel_aba', aba='inicio')

    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            # Corrigido: usar nome correto da rota com parâmetro
            return redirect('painel:painel_aba', aba='inicio')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    
    return render(request, 'usuarios/login.html')

# 🚪 Logout
def logout_view(request):
    logout(request)
    return redirect('usuarios:login')

# 🆕 Cadastro de novo usuário
def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar = request.POST.get('confirmar')

        if senha != confirmar:
            messages.error(request, "As senhas não coincidem.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe.")
        else:
            user = User.objects.create_user(username=username, email=email, password=senha)
            user.first_name = nome
            user.save()
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect('usuarios:login')

    return render(request, 'usuarios/cadastro.html')

# 👤 Edição de perfil
@login_required
def editar_perfil_view(request):
    user = request.user

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')

        if nome:
            user.first_name = nome
        if email:
            user.email = email
        user.save()
        messages.success(request, "Perfil atualizado com sucesso!")
        return redirect('usuarios:editar_perfil')

    return render(request, 'usuarios/editar_perfil.html', {'usuario': user})

# 🔑 Alteração de senha
@login_required
def alterar_senha_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Senha alterada com sucesso.")
            return redirect('usuarios:alterar_senha')
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'usuarios/alterar_senha.html', {'form': form})

# 🔒 Verifica se é superusuário
def eh_superuser(user):
    return user.is_superuser

# 🧑‍💻 Gerenciar usuários (somente superusuários)
@login_required
@user_passes_test(eh_superuser)
def gerenciar_usuarios_view(request):
    usuarios = User.objects.all().order_by('first_name')
    return render(request, 'usuarios/gerenciar.html', {'usuarios': usuarios})

# ✏️ Editar outro usuário (somente superusuários)
@login_required
@user_passes_test(eh_superuser)
def editar_usuario_view(request, user_id):
    usuario = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        usuario.first_name = request.POST.get('nome')
        usuario.email = request.POST.get('email')
        usuario.is_superuser = 'is_superuser' in request.POST
        usuario.save()

        LogUsuario.objects.create(
            executado_por=request.user,
            usuario_alvo=usuario,
            acao='editou'
        )

        messages.success(request, "Usuário atualizado com sucesso.")
        return redirect('usuarios:gerenciar_usuarios')

    return render(request, 'usuarios/editar_usuario.html', {'usuario': usuario})

# ❌ Excluir outro usuário (somente superusuários)
@login_required
@user_passes_test(eh_superuser)
def excluir_usuario_view(request, user_id):
    if request.user.id == user_id:
        messages.error(request, "Você não pode excluir a si mesmo.")
        return redirect('usuarios:gerenciar_usuarios')

    usuario_alvo = get_object_or_404(User, id=user_id)

    LogUsuario.objects.create(
        executado_por=request.user,
        usuario_alvo=usuario_alvo,
        acao='excluiu'
    )

    usuario_alvo.delete()
    messages.success(request, "Usuário excluído com sucesso.")
    return redirect('usuarios:gerenciar_usuarios')

# ✅ Visualizar logs de usuários (somente superusuários)
@login_required
@user_passes_test(eh_superuser)
def logs_usuarios_view(request):
    logs = LogUsuario.objects.select_related('executado_por', 'usuario_alvo').order_by('-data_hora')
    return render(request, 'usuarios/logs.html', {'logs': logs})
