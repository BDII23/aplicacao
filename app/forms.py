from django import forms
from .database.armazem import *
from .database.tipo_componente import * 
from .database.tipo_equipamento import * 
from .database.tipo_mao_obra import * 
from .database.componente import * 

class FormComponente(forms.Form):
    quantidade = forms.IntegerField(label='Quantidade', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    endereco_armazem = forms.ChoiceField(label='Endereco Armazem', choices=[('default', '-')], widget=forms.Select(attrs={'class': 'form-control'}))
    tipo_componente = forms.ChoiceField(label='Tipo de Componente', choices=[('default', '-')], widget=forms.Select(attrs={'class': 'form-control'}))
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super(FormComponente, self).__init__(*args, **kwargs)
        self.carregar_opcoes()

    def carregar_opcoes(self):
        tipos_componentes = readjson_tipo_componente()
        self.fields['tipo_componente'].choices = [(tipo['id'], tipo['tipo']) for tipo in tipos_componentes]

        armazens = readjson_armazem()
        self.fields['endereco_armazem'].choices = [(armazem['id'], armazem['endereco']) for armazem in armazens]
        
    def preencher_form(self, dados_form):
        self.fields['quantidade'].initial = dados_form['quantidade']
        self.fields['endereco_armazem'].initial = dados_form['endereco_armazem']
        self.fields['tipo_componente'].initial = dados_form['tipo_componente']
        self.fields['descricao'].initial = dados_form['descricao']



class FormFichaProducao(forms.Form):
    quantidade = forms.IntegerField(label='Quantidade Equipamentos', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    tipo_mao_obra = forms.ChoiceField(label='Tipo Mão de Obra', widget=forms.Select(attrs={'class': 'form-control'}))
    horas = forms.IntegerField(label='Horas', widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    componentes = forms.MultipleChoiceField(label='Componentes', widget=forms.SelectMultiple(attrs={'class': 'form-control'}))    
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea(attrs={'class': 'form-control'}))
    tipo_equipamento = forms.ChoiceField(label='Tipo de Equipamento', widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(FormFichaProducao, self).__init__(*args, **kwargs)
        self.carregar_opcoes()

    def carregar_opcoes(self):
        tipos_mao_obra = readjson_tipo_mao_obra()
        self.fields['tipo_mao_obra'].choices = [(tipo['id'], tipo['tipo']) for tipo in tipos_mao_obra]

        componentes = readjson_componente()
        self.fields['componentes'].choices = [(componente['id'], componente['descricao']) for componente in componentes]

        tipo_equipamento = readjson_tipo_equipamento()
        self.fields['tipo_equipamento'].choices = [(tipo['id'], tipo['tipo']) for tipo in tipo_equipamento]

        
    def preencher_form(self, dados_form):
        return