from django import forms
from ..database.guia_remessa_cliente import * 


class FormClienteRemessa(forms.Form):
    equipamentos = forms.MultipleChoiceField(label='Equipamentos para Receber', widget=forms.SelectMultiple(attrs={'class': 'form-control'}))    
    data_envio = forms.DateField(label='Data de Envio',widget=forms.DateInput(attrs={'class': 'form-control datepicker'}))
    data_entrega = forms.DateField(label='Data de Entrega', widget=forms.DateInput(attrs={'class': 'form-control datepicker'}))
    endereco_origem = forms.CharField(label='Endereço de Origem', widget=forms.TextInput(attrs={'class': 'form-control'}))
    endereco_chegada = forms.CharField(label='Endereço de Chegada', widget=forms.TextInput(attrs={'class': 'form-control'}))
    fatura_descricao = forms.CharField(label='Descrição da Fatura', widget=forms.Textarea(attrs={'class': 'form-control'}))


    def __init__(self, *args, **kwargs):
        super(FormClienteRemessa, self).__init__(*args, **kwargs)
        self.carregar_opcoes()

    def carregar_opcoes(self):
        encomenda_equipamentos = readjson_guia_remessa_clientes_componentes()
        self.fields['equipamentos'].choices = [(encomenda_equipamento['detalhe_id'], encomenda_equipamento['tipo_equipamento'] + " (encomenda " + str(encomenda_equipamento['encomenda_id']) + ")") for encomenda_equipamento in encomenda_equipamentos]

        
    def preencher_form(self, dados_form):
        self.fields['equipamentos'].initial = dados_form['equipamentos']
        self.fields['data_envio'].initial = dados_form['data_envio']
        self.fields['data_entrega'].initial = dados_form['data_entrega']
        self.fields['endereco_origem'].initial = dados_form['endereco_origem']
        self.fields['endereco_chegada'].initial = dados_form['endereco_chegada']
        self.fields['fatura_descricao'].initial = dados_form['fatura_descricao']