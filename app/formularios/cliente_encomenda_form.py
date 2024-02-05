from django import forms
import json
from ..database.equipamento import * 
from ..database.cliente import * 


class FormClienteEncomenda(forms.Form):
    equipamentos = forms.MultipleChoiceField(label='Equipamentos para Encomendar', widget=forms.SelectMultiple(attrs={'class': 'form-control'}))    
    clientes = forms.ChoiceField(label='Clientes', widget=forms.Select(attrs={'class': 'form-control'}))


    def __init__(self, *args, **kwargs):
        super(FormClienteEncomenda, self).__init__(*args, **kwargs)
        self.carregar_opcoes()

    def carregar_opcoes(self):
        equipamentos = readjson_equipamento()
        self.fields['equipamentos'].choices = [(equipamento['id'], equipamento['tipo_equipamento'][0]['tipo']) for equipamento in equipamentos]

        clientes = readjson_cliente()
        self.fields['clientes'].choices = [(cliente['id'], cliente['nome']) for cliente in clientes]
        
    def preencher_form(self, dados_form):
        self.fields['equipamentos'].initial = dados_form['equipamentos']
        self.fields['clientes'].initial = dados_form['clientes']
        

class FormClienteEncomendaImportar(forms.Form):
    json = forms.CharField(label='JSON', widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    def __init__(self, *args, **kwargs):
        super(FormClienteEncomendaImportar, self).__init__(*args, **kwargs)
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