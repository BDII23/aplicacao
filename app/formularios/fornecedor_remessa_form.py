from django import forms
import json
from ..database.guia_remessa_fornecedor import * 


class FormFornecedorRemessa(forms.Form):
    componentes = forms.MultipleChoiceField(label='Componentes para Receber', widget=forms.SelectMultiple(attrs={'class': 'form-control'}))    
    data_envio = forms.DateField(label='Data de Envio',widget=forms.DateInput(attrs={'class': 'form-control datepicker'}))
    data_entrega = forms.DateField(label='Data de Entrega', widget=forms.DateInput(attrs={'class': 'form-control datepicker'}))
    endereco_origem = forms.CharField(label='Endereço de Origem', widget=forms.TextInput(attrs={'class': 'form-control'}))
    endereco_chegada = forms.CharField(label='Endereço de Chegada', widget=forms.TextInput(attrs={'class': 'form-control'}))
    fatura_descricao = forms.CharField(label='Descrição da Fatura', widget=forms.Textarea(attrs={'class': 'form-control'}))


    def __init__(self, *args, **kwargs):
        super(FormFornecedorRemessa, self).__init__(*args, **kwargs)
        self.carregar_opcoes()

    def carregar_opcoes(self):
        encomenda_componentes = readjson_guia_remessa_fornecedores_componentes()
        self.fields['componentes'].choices = [(encomenda_componente['detalhe_id'], encomenda_componente['componente_descricao'] + " (encomenda " + str(encomenda_componente['encomenda_id']) + ")") for encomenda_componente in encomenda_componentes]

        
    def preencher_form(self, dados_form):
        self.fields['componentes'].initial = dados_form['componentes']