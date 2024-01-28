from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..database.componente import *
from ..database.armazem import *
from ..database.tipo_componente import *
from ..forms import *

def fornecedores_listar(request):
    try:
        componentes = readjson_componente()
        return render(request, 'componentes/listar.html', {'componentes': componentes})
    except Exception as e:
        return HttpResponse(e)

def fornecedores_registar(request):
    try:
        if request.method == 'POST':
            form = FormComponente(request.POST)
            if form.is_valid():
                create_componente(form.cleaned_data['descricao'], 
                    form.cleaned_data['quantidade'], 
                    form.cleaned_data['endereco_armazem'], 
                    form.cleaned_data['tipo_componente'])
                return redirect("/")
        else:
            form = FormComponente()
        return render(request, 'componentes/registar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)

def fornecedores_atualizar(request, id):
    try:
        if request.method == 'POST':
            form = FormComponente(request.POST)
            if form.is_valid():
                update_componente(id,
                    form.cleaned_data['descricao'], 
                    form.cleaned_data['quantidade'], 
                    form.cleaned_data['endereco_armazem'], 
                    form.cleaned_data['tipo_componente'])
                return redirect("/")
        else:
            form = FormComponente()
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