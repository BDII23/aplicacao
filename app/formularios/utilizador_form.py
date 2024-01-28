from django import forms
from ..database.utilizador_perfil import *


class FormUtilizadores(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)
    nome = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sobrenome = forms.CharField(label='Sobrenome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    perfil = forms.ChoiceField(label='Perfil', choices=[('default', '-')], widget=forms.Select(attrs={'class': 'form-control'}))
    
    def __init__(self, *args, **kwargs):
        super(FormUtilizadores, self).__init__(*args, **kwargs)
        self.carregar_opcoes()

    def preencher_form(self, dados_form):
        self.fields['email'].initial = dados_form['email']
        self.fields['nome'].initial = dados_form['nome']
        self.fields['sobrenome'].initial = dados_form['sobrenome']
        self.fields['perfil'].initial = dados_form['perfil']
    
    def carregar_opcoes(self):
        perfis = readjson_utilizador_perfil()
        self.fields['perfil'].choices = [(perfil['id'], perfil['perfil']) for perfil in perfis]