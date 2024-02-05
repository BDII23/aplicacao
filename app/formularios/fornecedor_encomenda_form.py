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


class FormFornecedorEncomendaImportar(forms.Form):
    json = forms.CharField(label='JSON', widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    def __init__(self, *args, **kwargs):
        super(FormFornecedorEncomendaImportar, self).__init__(*args, **kwargs)
        self.preencher_default()

    def clean_jsonfield(self):
        jdata = self.cleaned_data['json']
        try:
            return json.loads(jdata)
        except:
            raise forms.ValidationError("Dados inválidos")

    def preencher_default(self):
        self.fields['json'].initial = "[\n\t{\n\n\t}\n]"
    
    def preencher(self, json):
        self.fields['json'].initial = json
