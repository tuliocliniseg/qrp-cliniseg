from django import forms
from .models import Pergunta, Fator, Acao

class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ['texto', 'fator']
        widgets = {
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fator': forms.Select(attrs={'class': 'form-select'}),
        }

class FatorAcaoForm(forms.ModelForm):
    class Meta:
        model = Fator
        fields = ['nome']  # Apenas nome editável
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AcaoForm(forms.ModelForm):
    class Meta:
        model = Acao
        fields = ['descricao']  # Somente descrição editável
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
