from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..database.equipamento import *
from ..database.mg_equipamento_producao import *


def equipamentos_listar(request):
    try:
        equipamentos = readjson_equipamento()
        return render(request, 'equipamentos/listar.html', {'equipamentos': equipamentos})
    except Exception as e:
        return HttpResponse(e)

# n terminado
def equipamentos_registar(request):
    try:
        equipamentos = create_equipamento()
        return render(request, 'equipamentos/registar.html', {'equipamentos': equipamentos})
        
    except Exception as e:
        return HttpResponse(e)

def equipamentos_listar_id(request, id):
    try:
        equipamento = readone_equipamento(id)
        equipamento_producao = readone_equipamento_producao(id)
        print("equipamentos")
        print(equipamento)
        print("equipamento_producao")
        print(equipamento_producao)
        return render(request, 'equipamentos/listar_id.html', {'equipamento': equipamento, 'equipamento_producao': equipamento_producao})
    except Exception as e:
        return HttpResponse(e)

def equipamentos_atualizar(request, id):
    try:
        return
    except Exception as e:
        return HttpResponse(e)