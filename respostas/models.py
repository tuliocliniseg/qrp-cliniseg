from django.db import models
from empresas.models import Empresa, Setor

class Resposta(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)  # Relaciona ao setor correto
    sexo = models.CharField(max_length=20)
    faixa_etaria = models.CharField(max_length=50)

    # Campos para as 35 perguntas do questionário
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()
    q11 = models.IntegerField()
    q12 = models.IntegerField()
    q13 = models.IntegerField()
    q14 = models.IntegerField()
    q15 = models.IntegerField()
    q16 = models.IntegerField()
    q17 = models.IntegerField()
    q18 = models.IntegerField()
    q19 = models.IntegerField()
    q20 = models.IntegerField()
    q21 = models.IntegerField()
    q22 = models.IntegerField()
    q23 = models.IntegerField()
    q24 = models.IntegerField()
    q25 = models.IntegerField()
    q26 = models.IntegerField()
    q27 = models.IntegerField()
    q28 = models.IntegerField()
    q29 = models.IntegerField()
    q30 = models.IntegerField()
    q31 = models.IntegerField()
    q32 = models.IntegerField()
    q33 = models.IntegerField()
    q34 = models.IntegerField()
    q35 = models.IntegerField()

    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.empresa.nome} - {self.setor.nome} ({self.data_envio.strftime('%d/%m/%Y')})"
