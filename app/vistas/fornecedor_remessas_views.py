from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..database.guia_remessa_fornecedor import *


def fornecedores_remessas_listar(request):
    try:
        guia_remessa = readjson_guia_remessa_fornecedor()
        print(guia_remessa)
        return render(request, 'fornecedor_remessas/listar.html', {'guia_remessa': guia_remessa})
    except Exception as e:
        return HttpResponse(e)

def fornecedores_remessas_listar_id(request, id):
    try:
        remessa = readone_guia_remessa_fornecedor(id)
        return render(request, 'fornecedor_remessas/listar_id.html', {'remessa': remessa})
    except Exception as e:
        return HttpResponse(e)

def fornecedores_remessas_registar():
	return


def fornecedores_remessas_atualizar():
	return