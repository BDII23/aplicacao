from django import forms

class FormComponenteRegistrar(forms.Form):
    quantidade = forms.IntegerField(label='Quantidade', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    endereco_armazem = forms.ChoiceField(label='Endereco Armazem', choices=[('default', '-')], widget=forms.Select(attrs={'class': 'form-control'}))
    tipo_componente = forms.ChoiceField(label='Tipo de Componente', choices=[('default', '-')], widget=forms.Select(attrs={'class': 'form-control'}))
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea(attrs={'class': 'form-control'}))
