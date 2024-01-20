from django.shortcuts import render, redirect
from django.http import HttpResponse
from .database.detalhe_encomenda_fornecedor import *
from .database.componente import *
from .database.armazem import *
from .database.equipamento import *
from .database.tipo_componente import *
from .database.encomenda_cliente import * 
import logging
from .forms import *

logger = logging.getLogger(__name__)

def pagina_inicial(request):
    return render(request, 'index.html')

def componentes_listar(request):
    try:
        componentes = readjson_componente()
        return render(request, 'componentes/listar.html', {'componentes': componentes})
    except Exception as e:
        return HttpResponse(e)

def componentes_registrar(request):
    try:
        if request.method == 'POST':
            form = FormComponenteRegistrar(request.POST)
            if form.is_valid():
                create_componente(form.cleaned_data['descricao'], 
                    form.cleaned_data['quantidade'], 
                    form.cleaned_data['endereco_armazem'], 
                    form.cleaned_data['tipo_componente'])
                return redirect("/")
        else:
            form = FormComponenteRegistrar()
        return render(request, 'componentes/registrar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)

def componentes_atualizar(request, id):
    try:
        if request.method == 'POST':
            form = FormComponenteRegistrar(request.POST)
            if form.is_valid():
                update_componente(id,
                    form.cleaned_data['descricao'], 
                    form.cleaned_data['quantidade'], 
                    form.cleaned_data['endereco_armazem'], 
                    form.cleaned_data['tipo_componente'])
                return redirect("/")
        else:
            form = FormComponenteRegistrar()
            componente = readone_componente(id)
            print("opa")
            print(componente)
            form.preencher_form({
                'quantidade': componente['quantidade'],
                'endereco_armazem': componente['armazem_id'],
                'tipo_componente': componente['tipo_id'],
                'descricao': componente['descricao']
            })
        return render(request, 'componentes/atualizar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)
    
'''def componentes_apagar(request, id):
    try:
        delete_componente(id)
        return redirect("/")
    except Exception as e:
        return HttpResponse(e)'''
    

def compras_historico_listar(request):
    try:
        compras = read_encomenda_cliente()
        print("Detalhes de compras de cliente : %s", compras)

        return render(request, 'compras/historicocompras.html', {'compras': compras})
    
    except Exception as e:
        return HttpResponse(e)
    

# Equipamentos #
    
def equipamentos_listar(request):
    try:
        equipamentos = readjson_equipamento()
        return render(request, 'equipamentos/equipamentos-listar.html', {'lista_equipamentos': equipamentos})
    except Exception as e:
        return HttpResponse(e)

# n terminado
def equipamento_registar(request):
    try:
        equipamentos = create_equipamento()
        return render(request, 'equipamentos/equipamento-register.html', {'equipamentos': equipamentos})
        
    except Exception as e:
        return HttpResponse(e)


    
    
     
    
    
