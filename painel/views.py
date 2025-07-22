from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.db import models

from empresas.models import Empresa, Setor
from respostas.models import Resposta  # IMPORTANTE: importar para consultas
from .models import Pergunta, Fator, Acao, LogAcao
from .forms import PerguntaForm, FatorAcaoForm, AcaoForm  # Inclui AcaoForm


@login_required
def painel_view(request, aba):
    usuario = request.user
    context = {'usuario': usuario}

    if aba == 'inicio':
        return render(request, 'painel/inicio.html', context)

    elif aba == 'dados':
        # Dados gerais
        total_empresas = Empresa.objects.count()
        total_setores = Setor.objects.count()
        total_colaboradores = Setor.objects.aggregate(total=models.Sum('num_funcionarios'))['total'] or 0
        total_fatores = 18  # fixo conforme domínio

        # NOVO: Dados detalhados por empresa e setor com andamento das respostas
        empresas = Empresa.objects.prefetch_related('setores').all()
        dados_empresas = []
        for empresa in empresas:
            setores_info = []
            for setor in empresa.setores.all():
                num_funcionarios = setor.num_funcionarios
                respostas_count = Resposta.objects.filter(setor=setor).count()
                percentual = 0
                if num_funcionarios > 0:
                    percentual = (respostas_count / num_funcionarios) * 100

                setores_info.append({
                    'nome_setor': setor.nome_setor,
                    'num_funcionarios': num_funcionarios,
                    'respostas_count': respostas_count,
                    'percentual': round(percentual, 2),
                })

            dados_empresas.append({
                'nome_empresa': empresa.nome,
                'total_funcionarios': empresa.total_funcionarios,
                'setores': setores_info,
            })

        context.update({
            'total_empresas': total_empresas,
            'total_setores': total_setores,
            'total_colaboradores': total_colaboradores,
            'total_fatores': total_fatores,
            'dados_empresas': dados_empresas,  # dados para template
        })
        return render(request, 'painel/dados.html', context)

    elif aba == 'relatorios':
        empresas = Empresa.objects.all().order_by('nome')
        slug = request.GET.get('empresa_slug')
        empresa = None
        if slug:
            empresa = Empresa.objects.filter(slug=slug).first()
        context['empresas'] = empresas
        context['empresa'] = empresa  # para template mostrar botões
        return render(request, 'painel/relatorios.html', context)

    elif aba == 'configuracoes':
        return render(request, 'painel/configuracoes.html', context)

    else:
        return redirect('painel:painel_aba', aba='inicio')


@login_required
def listar_perguntas(request):
    perguntas = Pergunta.objects.select_related('fator').all()
    return render(request, 'painel/listar_perguntas.html', {'perguntas': perguntas})


@login_required
def editar_pergunta(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, id=pergunta_id)
    if request.method == 'POST':
        form = PerguntaForm(request.POST, instance=pergunta)
        if form.is_valid():
            form.save()
            return redirect('painel:listar_perguntas')
    else:
        form = PerguntaForm(instance=pergunta)
    return render(request, 'painel/editar_pergunta.html', {'form': form})


@login_required
def listar_fatores(request):
    fatores = Fator.objects.all().order_by('ordem')
    return render(request, 'painel/listar_fatores.html', {'fatores': fatores})


@login_required
def editar_fator_acao(request, fator_id):
    fator = get_object_or_404(Fator, id=fator_id)

    # Ordenação personalizada para ações por classificação
    ordem_classificacao = models.Case(
        models.When(classificacao='Baixo', then=1),
        models.When(classificacao='Moderado', then=2),
        models.When(classificacao='Elevado', then=3),
        models.When(classificacao='Crítico', then=4),
        default=5,
        output_field=models.IntegerField(),
    )
    acoes = Acao.objects.filter(fator=fator).order_by(ordem_classificacao, 'id')

    ordens = ['Baixo', 'Moderado', 'Elevado', 'Crítico']  # Ordem fixa para template

    if request.method == 'POST':
        fator_form = FatorAcaoForm(request.POST, instance=fator)
        if fator_form.is_valid():
            fator_form.save()

            # Atualiza as descrições das ações com os dados do formulário
            for acao in acoes:
                campo_desc = f'acao_descricao_{acao.id}'
                nova_descricao = request.POST.get(campo_desc)
                if nova_descricao is not None and acao.descricao != nova_descricao:
                    acao.descricao = nova_descricao
                    acao.save()

            return redirect('painel:listar_fatores')
    else:
        fator_form = FatorAcaoForm(instance=fator)

    return render(request, 'painel/editar_fator_acao.html', {
        'fator_form': fator_form,
        'acoes': acoes,
        'fator': fator,
        'ordens': ordens,
    })


@login_required
def editar_acao(request, acao_id):
    acao = get_object_or_404(Acao, id=acao_id)
    if request.method == 'POST':
        form = AcaoForm(request.POST, instance=acao)
        if form.is_valid():
            form.save()
            return redirect('painel:editar_fator_acao', fator_id=acao.fator.id)
    else:
        form = AcaoForm(instance=acao)
    return render(request, 'painel/editar_acao.html', {'form': form, 'acao': acao})


def superuser_required(view_func):
    """Decorator para permitir acesso apenas a superusuários."""
    return login_required(user_passes_test(lambda u: u.is_superuser)(view_func))


@superuser_required
def logs_usuarios_view(request):
    logs = LogAcao.objects.select_related('executado_por', 'usuario_alvo').order_by('-data_hora')[:100]
    return render(request, 'painel/logs_usuarios.html', {'logs': logs})
