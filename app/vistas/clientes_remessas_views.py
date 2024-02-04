from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..database.guia_remessa_cliente import *


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
	return


def clientes_remessas_atualizar(request, id):
	return