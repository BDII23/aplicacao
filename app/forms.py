from django import forms
from .database.armazem import *
from .database.tipo_componente import * 

class FormComponenteRegistrar(forms.Form):
    quantidade = forms.IntegerField(label='Quantidade', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    endereco_armazem = forms.ChoiceField(label='Endereco Armazem', choices=[('default', '-')], widget=forms.Select(attrs={'class': 'form-control'}))
    tipo_componente = forms.ChoiceField(label='Tipo de Componente', choices=[('default', '-')], widget=forms.Select(attrs={'class': 'form-control'}))
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super(FormComponenteRegistrar, self).__init__(*args, **kwargs)
        self.carregar_opcoes()

    def carregar_opcoes(self):
        tipos_componentes = readjson_tipo_componente()
        self.fields['tipo_componente'].choices = [(tipo['id'], tipo['tipo']) for tipo in tipos_componentes]

        armazens = readjson_armazem()
        self.fields['endereco_armazem'].choices = [(armazem['id'], armazem['endereco']) for armazem in armazens]