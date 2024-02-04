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
from .vistas.fornecedor_encomendas_views import *
from .vistas.fornecedor_remessas_views import *
from .vistas.clientes_encomendas_views import *
from .vistas.clientes_remessas_views import *



#from .database.mg_equipamento_producao import *

def pagina_inicial(request):
    return render(request, 'index.html')    