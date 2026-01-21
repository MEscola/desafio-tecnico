from django import forms
from datetime import date
from .models import Projects, SubItem
from users.models import User as Usuario



class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get('data_inicio')
        data_fim = cleaned_data.get('data_fim')
        dono = cleaned_data.get('dono_projeto')

        if not dono:
                self.add_error('dono_projeto', "Você deve selecionar um dono para o projeto da lista.")

        if data_inicio and data_fim:
            if data_fim < data_inicio:
                self.add_error('data_fim', "A data de fim não pode ser anterior à data de início.")
            
        return cleaned_data

    
class SubItemForm(forms.ModelForm):
    class Meta:
        model = SubItem
        fields = ['titulo', 'descricao', 'responsavel', 'status', 'prazo']
        widgets = {
            'prazo': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['responsavel'].queryset = Usuario.objects.all()

    
