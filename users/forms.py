from django import forms
from .models import User
from .validators import validade_telefone, validate_cpf     
from datetime import datetime

class UserForm(forms.ModelForm):
    # Força o aceite a ser obrigatório no nível do formulário
    aceite = forms.BooleanField(
        required=True, 
        error_messages={'required': 'Você deve aceitar os termos e condições.'}
    )

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'telefone': forms.TextInput(attrs={'class': 'phone-mask'}),
            'cpf': forms.TextInput(attrs={'class': 'cpf-mask'}),
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not validate_cpf(cpf):
            raise forms.ValidationError("CPF inválido")
        return cpf
    
    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

    def clean_aceite(self):
        aceite = self.cleaned_data.get('aceite')
        if not aceite:
            raise forms.ValidationError("Você deve aceitar os termos e condições.")
        return aceite