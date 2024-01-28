from django import forms
from ..database.armazem import *
from ..database.tipo_componente import * 


class FormFornecedores(forms.Form):
    nome = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telefone = forms.IntegerField(label='Telefone', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    nif = forms.IntegerField(label='Nif', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    endereco = forms.CharField(label='Endereço', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    def __init__(self, *args, **kwargs):
        super(FormFornecedores, self).__init__(*args, **kwargs)

    def preencher_form(self, dados_form):
        self.fields['nome'].initial = dados_form['nome']
        self.fields['email'].initial = dados_form['email']
        self.fields['telefone'].initial = dados_form['telefone']
        self.fields['nif'].initial = dados_form['nif']
        self.fields['endereco'].initial = dados_form['endereco']
