# respostas/management/commands/gerar_respostas_simuladas.py

from django.core.management.base import BaseCommand
from empresas.models import Empresa, Setor
from respostas.models import Resposta
import random

class Command(BaseCommand):
    help = 'Gera respostas simuladas com valores de 1 a 5 para empresas e setores cadastrados'

    def handle(self, *args, **options):
        empresas = Empresa.objects.prefetch_related("setores").all()
        if not empresas.exists():
            self.stdout.write(self.style.ERROR("❌ Nenhuma empresa encontrada."))
            return

        for empresa in empresas:
            setores = empresa.setores.all()
            for setor in setores:
                for _ in range(10):  # 10 colaboradores simulados por setor
                    sexo = random.choice(['Masculino', 'Feminino'])
                    faixa_etaria = random.choice(['18 a 25', '26 a 35', '36 a 45', '46 a 55', '56 ou mais'])

                    respostas = {}
                    for q in range(1, 36):
                        respostas[f'q{q}'] = random.randint(1, 5)  # Corrigido: q1, q2, ..., q35

                    Resposta.objects.create(
                        empresa=empresa,
                        setor=setor,  # CORRETO: passando o objeto Setor, e não o nome
                        sexo=sexo,
                        faixa_etaria=faixa_etaria,
                        **respostas
                    )

        self.stdout.write(self.style.SUCCESS("✅ Respostas simuladas geradas com sucesso!"))
