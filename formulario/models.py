from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=255, unique=True)  # Nome deve ser único
    cnpj = models.CharField(max_length=18, unique=True)   # CNPJ com máscara, também único
    slug = models.SlugField(max_length=100, unique=True)  # Slug para URLs amigáveis

    @property
    def total_funcionarios(self):
        # Soma total dos funcionários de todos os setores da empresa
        return sum(setor.num_funcionarios for setor in self.setores.all())

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ['nome']


class Setor(models.Model):
    empresa = models.ForeignKey(
        Empresa,
        related_name='setores',           # Permite acessar empresa.setores.all()
        on_delete=models.CASCADE
    )
    nome_setor = models.CharField(max_length=255)         # Nome do setor
    num_funcionarios = models.PositiveIntegerField(default=0)  # Número de funcionários no setor

    def __str__(self):
        return f"{self.nome_setor} ({self.empresa.nome})"

    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"
        ordering = ['nome_setor']
