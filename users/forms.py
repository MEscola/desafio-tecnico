from django import forms
from .models import User
from .validators import validade_telefone, validate_cpf     
from datetime import datetime

class UserForm(forms.ModelForm):
    # Forçamos o aceite a ser obrigatório no nível do formulário
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
        }

    
    def clean_data_nascimento(self):
        data = self.cleaned_data.get('data_nascimento')
        if data and data > datetime.now().date():
            raise forms.ValidationError("A data de nascimento não pode ser no futuro.")
        return data
        
    def cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not validate_cpf(cpf):
            raise forms.ValidationError("CPF inválido")
        return cpf

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if not telefone:
            raise forms.ValidationError("Telefone inválido")
        
        validade_telefone(telefone) 
        return telefone

    def clean_aceite(self):
        aceite = self.cleaned_data.get('aceite')
        if not aceite:
            raise forms.ValidationError("Você deve aceitar os termos e condições.")
        return aceite