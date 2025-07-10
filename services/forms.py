# services/forms.py

from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        # Definimos os campos que aparecerão no formulário
        fields = ['titulo', 'descricao', 'imagem', 'categoria', 'duracao', 'preco']
        
        # O 'widgets' é a parte mágica. Aqui, associamos atributos HTML a cada campo.
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ex: Podologia Tradicional'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4
            }),
            'imagem': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            # Para o campo 'categoria', Django usará um <select> por padrão.
            # Nós só precisamos adicionar a classe do Bootstrap para estilizá-lo.
            'categoria': forms.Select(attrs={
                'class': 'form-select'  # 'form-select' é a classe Bootstrap para dropdowns
            }),
            'duracao': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Em minutos'
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00'
            }),
        }