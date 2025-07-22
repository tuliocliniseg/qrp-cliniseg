from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    cnpj = models.CharField(max_length=18, unique=True)  # 14 ou 18 com máscara
    slug = models.SlugField(unique=True, max_length=100)

    @property
    def total_funcionarios(self):
        # Corrigido para usar o nome correto do campo do Setor
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
        related_name='setores',
        on_delete=models.CASCADE
    )
    nome_setor = models.CharField(max_length=255)
    num_funcionarios = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nome_setor} ({self.empresa.nome})"

    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"
        ordering = ['nome_setor']
