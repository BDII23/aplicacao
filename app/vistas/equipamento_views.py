from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..database.equipamento import *
from ..database.mg_equipamento_producao import *
from ..forms import *
from ..utils import corrigir_json

def equipamentos_listar(request):
    try:
        equipamentos = readjson_equipamento()
        return render(request, 'equipamentos/listar.html', {'equipamentos': equipamentos})
    except Exception as e:
        return HttpResponse(e)

def equipamentos_listar_id(request, id):
    try:
        equipamento = readone_equipamento(id)
        equipamento_producao = readone_equipamento_producao(id)
        return render(request, 'equipamentos/listar_id.html', {'equipamento': equipamento, 'equipamento_producao': equipamento_producao})
    except Exception as e:
        return HttpResponse(e)

def equipamentos_registar(request):
    try:
        if request.method == 'POST':
            form = FormEquipamentos(request.POST)
            if form.is_valid():
                equipamento_id = create_equipamento(form.cleaned_data['tipo_equipamento'])
                print(equipamento_id)
                create_equipamento_producao(equipamento_id, form.clean_jsonfield())
                return redirect("/")
        else:
            form = FormEquipamentos()
        return render(request, 'equipamentos/registar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)

def equipamentos_atualizar(request, id):
    try:
        if request.method == 'POST':
            form = FormEquipamentos(request.POST)
            if form.is_valid():
                update_equipamento(id, form.cleaned_data['tipo_equipamento'])
                update_equipamento_producao(id, form.clean_jsonfield())
                return redirect("/")
        else:
            form = FormEquipamentos()
            equipamento = readone_equipamento(id)
            atributos = readone_equipamento_producao(id)
            
            print(atributos)
            
            aux_atributo = ""
            
            if atributos is None:
                aux_atributo = ""
            else:
                aux_atributo = corrigir_json(atributos['atributo'])
                
            form.preencher_form({
                'tipo_equipamento': equipamento['tipo_id'],
                'atributos_equipamento': aux_atributo
            })
        return render(request, 'fornecedores/atualizar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)