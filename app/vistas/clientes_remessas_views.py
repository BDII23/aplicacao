from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..database.guia_remessa_cliente import *
from ..forms import *


def clientes_remessas_listar(request):
    try:
        guia_remessa = readjson_guia_remessa_cliente()
        return render(request, 'cliente_remessas/listar.html', {'guia_remessa': guia_remessa})
    except Exception as e:
        return HttpResponse(e)

def clientes_remessas_listar_id(request, id):
    try:
        remessa = readone_guia_remessa_cliente(id)
        custo_total = custo_total_guia_remessa_cliente(id)
        return render(request, 'cliente_remessas/listar_id.html', {'remessa': remessa, 'custo_total': custo_total})
    except Exception as e:
        return HttpResponse(e)

def clientes_remessas_registar(request):
    try:
        if request.method == 'POST':
            form = FormClienteRemessa(request.POST)
            if form.is_valid():
                _detalhe_encomenda_id = form.cleaned_data['equipamentos']
                _data_envio = form.cleaned_data['data_envio']
                _data_entrega = form.cleaned_data['data_entrega']
                _endereco_origem = form.cleaned_data['endereco_origem']
                _endereco_chegada = form.cleaned_data['endereco_chegada']
                _fatura_descricao = form.cleaned_data['fatura_descricao']
                create_guia_remessa_cliente(_data_envio, _data_entrega, _endereco_origem, _endereco_chegada, 1, _fatura_descricao, _detalhe_encomenda_id)
                return redirect("/")
        else:
            form = FormClienteRemessa()
        return render(request, 'cliente_remessas/registar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)



def clientes_remessas_atualizar(request, id):
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