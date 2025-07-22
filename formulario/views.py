from django.shortcuts import render, get_object_or_404
from empresas.models import Empresa, Setor
from respostas.models import Resposta
from painel.models import Pergunta  # Modelo de perguntas do banco
from django.utils.timezone import now

def exibir_formulario(request):
    # 1. Captura o parâmetro GET 'empresa' para identificar a empresa pelo slug
    slug = request.GET.get('empresa')
    empresa = get_object_or_404(Empresa, slug=slug)

    # 2. Busca todas as perguntas da base, ordenadas por ID (normalmente 35)
    perguntas_qs = Pergunta.objects.all().order_by('id')

    if request.method == 'POST':
        # 3. Debug: mostra os dados enviados via POST (ajuda no desenvolvimento)
        print("Dados recebidos no POST:")
        print(request.POST)

        # 4. Captura o nome do setor selecionado (campo obrigatório no formulário)
        nome_setor = request.POST.get('setor')
        setor = get_object_or_404(Setor, nome_setor=nome_setor, empresa=empresa)

        # 5. Monta o dicionário inicial com dados básicos para criar o registro Resposta
        data = {
            'empresa': empresa,
            'setor': setor,
            'sexo': request.POST.get('sexo'),
            'faixa_etaria': request.POST.get('faixa_etaria'),
            'data_envio': now(),
        }

        # 6. Inicializa todas as respostas q1 a q35 como None para controle
        for i in range(1, 36):
            data[f'q{i}'] = None

        # 7. Atualiza as respostas a partir do POST convertendo para int e validando entre 1 e 5
        # Usa loop sequencial simples para garantir o nome correto dos campos q1...q35
        for i in range(1, 36):
            resposta = request.POST.get(f'q{i}')
            if resposta is not None:
                try:
                    valor = int(resposta)
                    # Validação estrita: só aceita valores entre 1 e 5
                    if 1 <= valor <= 5:
                        data[f'q{i}'] = valor
                    else:
                        print(f"Valor inválido para q{i}: {valor}")
                        data[f'q{i}'] = None
                except ValueError:
                    print(f"Erro conversão para q{i}: {resposta}")
                    data[f'q{i}'] = None
            else:
                data[f'q{i}'] = None

        # 8. Se alguma resposta estiver None, atribui zero para salvar (pode ajustar conforme regra de negócio)
        for i in range(1, 36):
            if data[f'q{i}'] is None:
                data[f'q{i}'] = 0

        # 9. Cria a instância Resposta com os dados validados
        obj = Resposta.objects.create(**data)
        print(f"Resposta salva no banco com ID: {obj.id}")

        # 10. Renderiza a página de agradecimento após salvar os dados
        return render(request, 'formulario_html/obrigado.html')

    # 11. Se método GET, prepara lista de tuplas (número da pergunta, texto) para o template
    perguntas = [(idx + 1, p.texto) for idx, p in enumerate(perguntas_qs)]

    # 12. Renderiza o formulário com empresa e perguntas para o template
    return render(request, 'formulario_html/formulario.html', {
        'empresa': empresa,
        'perguntas': perguntas,
    })
