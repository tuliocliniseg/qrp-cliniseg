from django import forms
from .models import Pergunta, Fator, Acao, TextoDiagnostico  # ⬅️ Adiciona o novo modelo aqui

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

# ✅ Novo formulário para editar os blocos de texto do diagnóstico
class TextoDiagnosticoForm(forms.ModelForm):
    class Meta:
        model = TextoDiagnostico
        fields = ['texto_inicial', 'texto_final']
        widgets = {
            'texto_inicial': forms.Textarea(attrs={
                'rows': 10,
                'class': 'form-control',
                'placeholder': 'Texto inicial do diagnóstico...'
            }),
            'texto_final': forms.Textarea(attrs={
                'rows': 12,
                'class': 'form-control',
                'placeholder': 'Texto final do diagnóstico...'
            }),
        }