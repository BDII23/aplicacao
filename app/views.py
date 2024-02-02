from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

# Vistas
from .vistas.componentes_views import *
from .vistas.fichaproducao_views import *
from .vistas.cliente_views import *
from .vistas.fornecedor_views import *
from .vistas.utilizador_views import *
from .vistas.equipamento_views import *



#from .database.mg_equipamento_producao import *

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
    



    
    
     
    
    
