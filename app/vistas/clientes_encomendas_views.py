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
            form = FormClienteEncomenda(request.POST)
            if form.is_valid():
                _equipamentos = form.cleaned_data['equipamentos']
                _cliente = form.cleaned_data['clientes']
                create_encomenda_cliente(_equipamentos, _cliente)
                return redirect("/")
        else:
            form = FormClienteEncomenda()
        return render(request, 'cliente_encomendas/registar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)



def clientes_encomendas_atualizar(request, id):
    try:
        if request.method == 'POST':
            form = FormClienteEncomenda(request.POST)
            if form.is_valid():
                _equipamentos = form.cleaned_data['equipamentos']
                _cliente = form.cleaned_data['clientes']
                update_encomenda_cliente(id, _equipamentos, _cliente)
                return redirect("/")
        else:
            form = FormClienteEncomenda()
            encomenda = readone_encomenda_cliente(id)
            equipamento_selected_arr = make_array_of_equipamentos_ids(encomenda)
            form.preencher_form({
                'equipamentos': equipamento_selected_arr,
    			'clientes': encomenda['cliente'][0]['id']
            })
        return render(request, 'cliente_encomendas/atualizar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)


def make_array_of_equipamentos_ids(data_encomenda):
    componente_selected_arr = []
    for detalhe in data_encomenda.get('detalhe_encomenda_cliente', []):
        componentes_array = detalhe.get('equipamento', [])
        for componente in componentes_array:
            id_componente = componente.get('id')
            if id_componente is not None:
                componente_selected_arr.append(id_componente)
    return componente_selected_arr