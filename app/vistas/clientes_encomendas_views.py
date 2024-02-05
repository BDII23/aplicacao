from ..database.encomenda_cliente import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..database.ficha_producao import *
from ..database.mg_equipamento_producao import *
from .fichaproducao_views import make_array_of_componentes_ids
from ..user import *
from ..forms import *


def clientes_encomendas_listar(request):
    try:
        encomendas_cliente = readjson_encomenda_cliente()
        print(encomendas_cliente)
        return render(request, 'cliente_encomendas/listar.html', {'encomendas_cliente': encomendas_cliente})
    except Exception as e:
        return HttpResponse(e)

def clientes_encomendas_listar_id(request, id):
    try:
        encomenda = readone_encomenda_cliente(id)
        return render(request, 'cliente_encomendas/listar_id.html', {'encomenda': encomenda})
    except Exception as e:
        return HttpResponse(e)

def clientes_encomendas_registar(request):
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
                create_equipamento_producao(ficha_id, _atributos_equipamento)
                return redirect("/")
        else:
            form = FormFichaProducao()
            form.fields['horas'].widget = forms.HiddenInput()
        return render(request, 'cliente_encomendas/registar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)

def clientes_encomendas_atualizar(request, id):
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
                equipamento_id = update_ficha_producao(id, _quantidade, _descricao, 0, get_logged_user(), _tipo_mao_obra, _tipo_equipamento, _componentes)
                update_equipamento_producao(equipamento_id, _atributos_equipamento)
                return redirect("/")
        else:
            form = FormFichaProducao()
            ficha_producao = readone_ficha_producao(id)
            componente_selected_arr = make_array_of_componentes_ids(ficha_producao)
            equipamento_producao = readone_equipamento_producao(ficha_producao['equipamento'][0]['id'])
            form.preencher_form({
                'quantidade': ficha_producao['quantidade_equipamentos'],
                'tipo_mao_obra': ficha_producao['tipo_mao_obra_id'],
                'horas': ficha_producao['horas'],
                'descricao': ficha_producao['descricao'],
                'equipamento': ficha_producao['equipamento'][0]['tipo_id'],
                'componentes': componente_selected_arr,
    			'atributos_equipamento': equipamento_producao['atributo'] if 'atributo' in equipamento_producao and equipamento_producao['atributo'] is not None else ""
            })
        return render(request, 'cliente_encomendas/atualizar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)