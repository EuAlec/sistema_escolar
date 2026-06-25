from django import forms

# ERRO ENCONTRADO: uso da importação <models> incorreta
# CORREÇÃO: implementado a importação correta
from portal.models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:  # A classe meta serve para configurar o form
        model = Professor  # Define o model que o form representa
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'registro',]
