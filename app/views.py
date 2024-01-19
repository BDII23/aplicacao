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

def experimentos(request):
    return

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
                descricao = form.cleaned_data['descricao']
                quantidade = form.cleaned_data['quantidade']
                endereco_armazem = form.cleaned_data['endereco_armazem']
                tipo_componente = form.cleaned_data['tipo_componente']

                create_componente(descricao, quantidade, tipo_componente, endereco_armazem)

                return redirect("/")
        else:
            form = FormComponenteRegistrar()
        tipos_componentes = readjson_tipo_componente()
        form.fields['tipo_componente'].choices = [(tipo['id'], tipo['tipo']) for tipo in tipos_componentes]
        armazens = readjson_armazem()
        form.fields['endereco_armazem'].choices = [(armazem['id'], armazem['endereco']) for armazem in armazens]

        return render(request, 'componentes/registrar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)

'''def componentes_registrar(request):
    try:
        form = FormComponenteRegistrar()
        tipos_componentes = readjson_tipo_componente()
        form.fields['tipo_componente'].choices = [(tipo['tipo'], tipo['tipo']) for tipo in tipos_componentes]
        return render(request, 'componentes/registrar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)'''

def componentes_atualizar(request):
    try:
        componentes = update_componente()
        print("Detalhes da Encomenda do Fornecedor: %s", componentes)

        return render(request, 'componentes/atualizar.html', {'componentes': componentes})
        
    except Exception as e:
        return HttpResponse(e)
    

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


    
    
     
    
    
