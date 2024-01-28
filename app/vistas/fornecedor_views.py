from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..database.fornecedor import *
from ..forms import *

def fornecedores_listar(request):
    try:
        fornecedores = readjson_fornecedor()
        return render(request, 'fornecedores/listar.html', {'fornecedores': fornecedores})
    except Exception as e:
        return HttpResponse(e)

def fornecedores_registar(request):
    try:
        if request.method == 'POST':
            form = FormFornecedores(request.POST)
            if form.is_valid():
                create_fornecedor(form.cleaned_data['nome'], 
                    form.cleaned_data['nif'], 
                    form.cleaned_data['email'], 
                    form.cleaned_data['telefone'], 
                    form.cleaned_data['endereco'])
                return redirect("/")
        else:
            form = FormFornecedores()
        return render(request, 'fornecedores/registar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)

def fornecedores_atualizar(request, id):
    try:
        if request.method == 'POST':
            form = FormFornecedores(request.POST)
            if form.is_valid():
                update_fornecedor(id,
                    form.cleaned_data['nome'], 
                    form.cleaned_data['nif'], 
                    form.cleaned_data['email'], 
                    form.cleaned_data['telefone'], 
                    form.cleaned_data['endereco'])
                return redirect("/")
        else:
            form = FormFornecedores()
            fornecedor = readone_fornecedor(id)
            print(fornecedor)
            form.preencher_form({
                'nome': fornecedor['nome'],
                'nif': fornecedor['nif'],
                'email': fornecedor['email'],
                'telefone': fornecedor['telefone'],
                'endereco': fornecedor['endereco']
            })
        return render(request, 'fornecedores/atualizar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)