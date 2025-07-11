from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    # Adicionamos um campo que não está no modelo
    subscribe_to_newsletter = forms.BooleanField(
        required=False, 
        initial=True, 
        label="Quero receber novidades e promoções por e-mail."
    )

    class Meta:
        model = Testimonial
        fields = ['name', 'email', 'body', 'subscribe_to_newsletter']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email (will not be published)'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your testimonial here...'}),
        }