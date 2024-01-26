from django.shortcuts import render, redirect
from django.http import HttpResponse
from .database.detalhe_encomenda_fornecedor import *
from .database.componente import *
from .database.armazem import *
from .database.equipamento import *
from .database.tipo_componente import *
from .database.encomenda_cliente import * 
from .forms import *

# Vistas
from .vistas.componentes_views import *
from .vistas.fichaproducao_views import *

def pagina_inicial(request):
    return render(request, 'index.html')    

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
def equipamentos_registar(request):
    try:
        equipamentos = create_equipamento()
        return render(request, 'equipamentos/equipamento-register.html', {'equipamentos': equipamentos})
        
    except Exception as e:
        return HttpResponse(e)


    
    
     
    
    
