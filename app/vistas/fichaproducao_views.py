from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..database.ficha_producao import *
from ..database.detalhe_ficha_producao import *
from ..database.tipo_mao_obra import *
from ..database.componente import *
from ..database.equipamento import *
from ..forms import *

def fichaproducoes_listar(request):
    try:
        ficha_producao = readjson_ficha_producao()
        print(ficha_producao)
        return render(request, 'ficha_producao/listar.html', {'ficha_producao': ficha_producao})
    except Exception as e:
        return HttpResponse(e)

def fichaproducoes_listar_id(request, id):
    try:
        ficha_producao = readone_ficha_producao(id)
        print(ficha_producao)
        return render(request, 'ficha_producao/listar_id.html', {'ficha_producao': ficha_producao})
    except Exception as e:
        return HttpResponse(e)

def fichaproducoes_registar(request):
    try:
        if request.method == 'POST':
            form = FormFichaProducao(request.POST)
            if form.is_valid():
                _quantidade = form.cleaned_data['quantidade']
                _tipo_mao_obra = form.cleaned_data['tipo_mao_obra']
                _descricao = form.cleaned_data['descricao']
                _componentes = form.cleaned_data['componentes']
                create_ficha_producao(_quantidade, _descricao, 0, )
                return redirect("/")
        else:
            form = FormFichaProducao()
            form.fields['horas'].widget = forms.HiddenInput()
        return render(request, 'ficha_producao/registar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)

def fichaproducoes_atualizar(request, id):
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
        return render(request, 'ficha_producao/atualizar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)