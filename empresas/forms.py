from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa  # Modelo ao qual este formulário está vinculado
        fields = ['nome', 'cnpj', 'slug']  # Campos que aparecerão no formulário

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),  # Campo "nome" com classe CSS para Bootstrap
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),  # Campo "cnpj" com estilo
            'slug': forms.TextInput(attrs={'class': 'form-control'}),  # Campo "slug" com estilo
        }
