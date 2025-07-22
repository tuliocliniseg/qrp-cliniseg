from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Empresa, Setor

def cadastrar_empresa(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        slug = request.POST.get('slug')

        # Validação básica dos campos obrigatórios
        if not nome or not cnpj or not slug:
            messages.error(request, 'Preencha todos os campos obrigatórios.')
            return render(request, 'empresas/cadastrar_empresa.html')

        # Criação da empresa
        empresa = Empresa.objects.create(nome=nome, cnpj=cnpj, slug=slug)

        # Captura listas de setores e funcionários enviados pelo formulário
        setores = request.POST.getlist('setores[]')
        funcionarios = request.POST.getlist('num_funcionarios[]')  # CORREÇÃO AQUI!

        # Para cada setor e quantidade de funcionários, cria o setor vinculado à empresa
        for s, f in zip(setores, funcionarios):
            try:
                f_int = int(f)
            except ValueError:
                f_int = 0  # Se a conversão falhar, salva como 0
            Setor.objects.create(empresa=empresa, nome_setor=s, num_funcionarios=f_int)

        messages.success(request, 'Empresa cadastrada com sucesso!')
        return redirect('empresas:listar_empresas')

    # Se GET, renderiza o formulário vazio para cadastro
    return render(request, 'empresas/cadastrar_empresa.html')


def listar_empresas(request):
    # Busca todas as empresas com seus setores relacionados para evitar queries extras
    empresas = Empresa.objects.prefetch_related('setores').all()
    return render(request, 'empresas/listar_empresas.html', {'empresas': empresas})


def editar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        slug = request.POST.get('slug')

        # Validação básica
        if not nome or not cnpj or not slug:
            messages.error(request, 'Preencha todos os campos obrigatórios.')
            return render(request, 'empresas/editar_empresa.html', {'empresa': empresa})

        # Atualiza os dados da empresa
        empresa.nome = nome
        empresa.cnpj = cnpj
        empresa.slug = slug
        empresa.save()

        # Remove setores antigos para evitar duplicatas
        empresa.setores.all().delete()

        # Captura listas atualizadas de setores e funcionários
        setores = request.POST.getlist('setores[]')
        funcionarios = request.POST.getlist('num_funcionarios[]')  # CORREÇÃO AQUI!

        # Cria novamente os setores atualizados
        for s, f in zip(setores, funcionarios):
            try:
                f_int = int(f)
            except ValueError:
                f_int = 0
            Setor.objects.create(empresa=empresa, nome_setor=s, num_funcionarios=f_int)

        messages.success(request, 'Empresa atualizada com sucesso!')
        return redirect('empresas:listar_empresas')

    # Se GET, renderiza formulário com dados atuais
    return render(request, 'empresas/editar_empresa.html', {'empresa': empresa})


def excluir_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)

    if request.method == 'POST':
        empresa.delete()
        messages.success(request, 'Empresa excluída com sucesso!')
        return redirect('empresas:listar_empresas')

    # Renderiza confirmação antes de excluir
    return render(request, 'empresas/confirmar_exclusao.html', {'empresa': empresa})


def painel_empresas_view(request):
    # Carrega empresas e setores para o painel principal
    empresas = Empresa.objects.prefetch_related('setores').all()
    return render(request, 'empresas/painel_empresas.html', {'empresas': empresas})
