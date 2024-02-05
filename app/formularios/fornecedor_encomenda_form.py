from django import forms
import json
from ..database.fornecedor import * 
from ..database.componente import * 


class FormFornecedorEncomenda(forms.Form):
    componentes = forms.MultipleChoiceField(label='Componentes para Encomendar', widget=forms.SelectMultiple(attrs={'class': 'form-control'}))    
    fornecedores = forms.ChoiceField(label='Fornecedor', widget=forms.Select(attrs={'class': 'form-control'}))


    def __init__(self, *args, **kwargs):
        super(FormFornecedorEncomenda, self).__init__(*args, **kwargs)
        self.carregar_opcoes()

    def carregar_opcoes(self):
        componentes = readjson_componente()
        self.fields['componentes'].choices = [(componente['id'], componente['descricao']) for componente in componentes]

        fornecedores = readjson_fornecedor()
        self.fields['fornecedores'].choices = [(fornecedor['id'], fornecedor['nome']) for fornecedor in fornecedores]

        
    def preencher_form(self, dados_form):
        self.fields['componentes'].initial = dados_form['componentes']
        self.fields['fornecedores'].initial = dados_form['fornecedores']