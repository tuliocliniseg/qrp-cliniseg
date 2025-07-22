from django.shortcuts import render, get_object_or_404
from empresas.models import Empresa, Setor
from respostas.models import Resposta
from painel.models import Pergunta
from django.utils.timezone import now

def exibir_formulario(request):
    slug = request.GET.get('empresa')
    empresa = get_object_or_404(Empresa, slug=slug)

    perguntas_qs = Pergunta.objects.all().order_by('id')

    if request.method == 'POST':
        nome_setor = request.POST.get('setor')
        setor = get_object_or_404(Setor, nome_setor=nome_setor, empresa=empresa)

        data = {
            'empresa': empresa,
            'setor': setor,
            'sexo': request.POST.get('sexo'),
            'faixa_etaria': request.POST.get('faixa_etaria'),
            'data_envio': now(),
        }

        for i in range(1, 36):
            resposta = request.POST.get(f'q{i}')
            try:
                valor = int(resposta)
                if 1 <= valor <= 5:
                    data[f'q{i}'] = valor
                else:
                    data[f'q{i}'] = 0
            except (TypeError, ValueError):
                data[f'q{i}'] = 0

        obj = Resposta.objects.create(**data)

        return render(request, 'formulario_html/obrigado.html')

    perguntas = [(idx + 1, p.texto) for idx, p in enumerate(perguntas_qs)]

    return render(request, 'formulario_html/formulario.html', {
        'empresa': empresa,
        'perguntas': perguntas,
    })
