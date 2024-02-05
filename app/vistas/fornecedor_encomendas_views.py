from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..user import *
from ..forms import *
from ..database.encomenda_fornecedor import *
from ..utils import tojson, corrigir_json



def fornecedores_encomendas_importar(request):
    try:
        if request.method == 'POST':
            form = FormFornecedorEncomendaImportar(request.POST)
            if form.is_valid():
                _json = form.cleaned_data['json']
                importar_encomenda_fornecedor(_json)
                return redirect("/")
        else:
            form = FormFornecedorEncomendaImportar()
        return render(request, 'fornecedor_encomendas/importar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)


def fornecedores_encomendas_exportar(request):
    try:
        form = FormFornecedorEncomendaImportar()
        exporte = exportar_encomenda_fornecedor()
        form.preencher(corrigir_json(exporte))
        return render(request, 'fornecedor_encomendas/exportar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)


def fornecedores_encomendas_listar(request):
    try:
        encomendas_fornecedor = readjson_encomenda_fornecedor()
        print(encomendas_fornecedor)
        return render(request, 'fornecedor_encomendas/listar.html', {'encomendas_fornecedor': encomendas_fornecedor})
    except Exception as e:
        return HttpResponse(e)

def fornecedores_encomendas_listar_id(request, id):
    try:
        encomenda = readone_encomenda_fornecedor(id)
        return render(request, 'fornecedor_encomendas/listar_id.html', {'encomenda': encomenda})
    except Exception as e:
        return HttpResponse(e)

def fornecedores_encomendas_registar(request):
    try:
        if request.method == 'POST':
            form = FormFornecedorEncomenda(request.POST)
            if form.is_valid():
                _componentes = form.cleaned_data['componentes']
                _fornecedor = form.cleaned_data['fornecedores']
                create_encomenda_fornecedor(_componentes, _fornecedor)
                return redirect("/")
        else:
            form = FormFornecedorEncomenda()
        return render(request, 'fornecedor_encomendas/registar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)



def fornecedores_encomendas_atualizar(request, id):
    try:
        if request.method == 'POST':
            form = FormFornecedorEncomenda(request.POST)
            if form.is_valid():
                _componentes = form.cleaned_data['componentes']
                _fornecedor = form.cleaned_data['fornecedores']
                update_encomenda_fornecedor(id, _componentes, _fornecedor)
                return redirect("/")
        else:
            form = FormFornecedorEncomenda()
            encomenda = readone_encomenda_fornecedor(id)
            componente_selected_arr = make_array_of_componentes_ids(encomenda)
            form.preencher_form({
                'componentes': componente_selected_arr,
    			'fornecedores': encomenda['fornecedor'][0]['id']
            })
        return render(request, 'fornecedor_encomendas/atualizar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)


def make_array_of_componentes_ids(data_encomenda):
    componente_selected_arr = []
    for detalhe in data_encomenda.get('detalhe_encomenda_fornecedor', []):
        componentes_array = detalhe.get('componente', [])
        for componente in componentes_array:
            id_componente = componente.get('id')
            if id_componente is not None:
                componente_selected_arr.append(id_componente)
    return componente_selected_arr