from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..database.cliente import *
from ..forms import *

def clientes_listar(request):
    try:
        clientes = readjson_cliente()
        return render(request, 'clientes/listar.html', {'clientes': clientes})
    except Exception as e:
        return HttpResponse(e)

def clientes_registar(request):
    try:
        if request.method == 'POST':
            form = FormClientes(request.POST) 
            if form.is_valid():
                create_cliente(form.cleaned_data['email'], 
                    form.cleaned_data['senha'], 
                    form.cleaned_data['nome'], 
                    form.cleaned_data['nif'])
                return redirect("/")
        else:
            form = FormClientes()
        return render(request, 'clientes/registar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)

def clientes_atualizar(request, id):
    try:
        if request.method == 'POST':
            form = FormClientes(request.POST)
            if form.is_valid():
                update_cliente(id,
                    form.cleaned_data['email'], 
                    form.cleaned_data['nome'], 
                    form.cleaned_data['nif'])
                return redirect("/")
        else:
            form = FormClientes()
            cliente = readone_cliente(id)
            print(cliente)
            form.preencher_form({
                'email': cliente['email'],
                'nome': cliente['nome'],
                'nif': cliente['nif']
            })
        return render(request, 'clientes/atualizar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)
    
    