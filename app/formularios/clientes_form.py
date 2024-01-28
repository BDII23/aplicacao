from django import forms
from ..database.armazem import *
from ..database.tipo_componente import * 


class FormClientes(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)
    nome = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    nif = forms.IntegerField(label='NIF', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    def __init__(self, *args, **kwargs):
        super(FormClientes, self).__init__(*args, **kwargs)

    def preencher_form(self, dados_form):
        self.fields['email'].initial = dados_form['email']
        self.fields['nome'].initial = dados_form['nome']
        self.fields['nif'].initial = dados_form['nif']
