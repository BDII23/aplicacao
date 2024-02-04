from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..database.encomenda_cliente import *


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

def clientes_encomendas_registar():
	return


def clientes_encomendas_atualizar():
	return