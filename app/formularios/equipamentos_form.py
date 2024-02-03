from django import forms
import json
from ..database.tipo_equipamento import * 


class FormEquipamentos(forms.Form):
    tipo_equipamento = forms.ChoiceField(label='Tipo de Equipamento', widget=forms.Select(attrs={'class': 'form-control'}))
    atributos_equipamento = forms.CharField(label='Atributos do Equipamento', widget=forms.Textarea(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(FormEquipamentos, self).__init__(*args, **kwargs)
        self.carregar_opcoes()
    
    def clean_jsonfield(self):
        jdata = self.cleaned_data['atributos_equipamento']
        try:
            return json.loads(jdata)
        except:
            raise forms.ValidationError("Dados inválidos nos Atributos do Equipamento")

    def carregar_opcoes(self):
        tipo_equipamento = readjson_tipo_equipamento()
        self.fields['tipo_equipamento'].choices = [(tipo['id'], tipo['tipo']) for tipo in tipo_equipamento]

        
    def preencher_form(self, dados_form):
        self.fields['tipo_equipamento'].initial = dados_form['tipo_equipamento']
        self.fields['atributos_equipamento'].initial = dados_form['atributos_equipamento']