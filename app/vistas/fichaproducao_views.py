from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..database.ficha_producao import *
from ..database.detalhe_ficha_producao import *
from ..database.tipo_mao_obra import *
from ..database.componente import *
from ..database.equipamento import *
from ..database.mg_equipamento_producao import *
from ..user import *
from ..forms import *

def fichaproducoes_listar(request):
    try:
        ficha_producao = readjson_ficha_producao()
        print(ficha_producao)
        return render(request, 'ficha_producao/listar.html', {'ficha_producao': ficha_producao})
    except Exception as e:
        return HttpResponse(e)

def fichaproducoes_listar_id(request, id):
    try:
        ficha_producao = readone_ficha_producao(id)
        print(ficha_producao)
        return render(request, 'ficha_producao/listar_id.html', {'ficha_producao': ficha_producao})
    except Exception as e:
        return HttpResponse(e)

def fichaproducoes_registar(request):
    try:
        if request.method == 'POST':
            form = FormFichaProducao(request.POST)
            if form.is_valid():
                _quantidade = form.cleaned_data['quantidade']
                _tipo_mao_obra = form.cleaned_data['tipo_mao_obra']
                _descricao = form.cleaned_data['descricao']
                _componentes = form.cleaned_data['componentes']
                _tipo_equipamento = form.cleaned_data['tipo_equipamento']
                _atributos_equipamento = form.clean_jsonfield()
                ficha_id = create_ficha_producao(_quantidade, _descricao, 0, get_logged_user(), _tipo_mao_obra, _tipo_equipamento, _componentes)
                print(_atributos_equipamento)
                create_equipamento_producao(_atributos_equipamento)
                return redirect("/")
        else:
            form = FormFichaProducao()
            form.fields['horas'].widget = forms.HiddenInput()
        return render(request, 'ficha_producao/registar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)




def fichaproducoes_atualizar(request, id):
    try:
        if request.method == 'POST':
            form = FormFichaProducao(request.POST)
            if form.is_valid():
                _quantidade = form.cleaned_data['quantidade']
                _tipo_mao_obra = form.cleaned_data['tipo_mao_obra']
                _descricao = form.cleaned_data['descricao']
                _componentes = form.cleaned_data['componentes']
                _tipo_equipamento = form.cleaned_data['tipo_equipamento']
                print(_quantidade, _descricao, 0, get_logged_user(), _tipo_mao_obra, _tipo_equipamento, _componentes)
                update_ficha_producao(id, _quantidade, _descricao, 0, get_logged_user(), _tipo_mao_obra, _tipo_equipamento, _componentes)
                return redirect("/")
        else:
            form = FormFichaProducao()
            ficha_producao = readone_ficha_producao(id)
            componente_selected_arr = make_array_of_componentes_ids(ficha_producao)
            
            print(ficha_producao)
            form.preencher_form({
                'quantidade': ficha_producao['quantidade_equipamentos'],
                'tipo_mao_obra': ficha_producao['tipo_mao_obra_id'],
                'horas': ficha_producao['horas'],
                'descricao': ficha_producao['descricao'],
                'equipamento': ficha_producao['equipamento'][0]['tipo_id'],
                'componentes': componente_selected_arr
            })
        return render(request, 'ficha_producao/atualizar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)


def make_array_of_componentes_ids(data_ficha_producao):
    componente_selected_arr = []
    for detalhe in data_ficha_producao.get('detalhe_ficha_producao', []):
        componentes_array = detalhe.get('componente', [])
        for componente in componentes_array:
            id_componente = componente.get('id')
            if id_componente is not None:
                componente_selected_arr.append(id_componente)
    return componente_selected_arr