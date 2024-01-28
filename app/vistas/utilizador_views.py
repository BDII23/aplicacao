from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..database.utilizador import *
from ..forms import *

def utilizadores_listar(request):
    try:
        utilizadores = readjson_utilizador()
        return render(request, 'utilizadores/listar.html', {'utilizadores': utilizadores})
    except Exception as e:
        return HttpResponse(e)

def utilizadores_registar(request):
    try:
        if request.method == 'POST':
            form = FormUtilizadores(request.POST)
            if form.is_valid():
                create_utilizador(form.cleaned_data['email'], 
                    form.cleaned_data['senha'], 
                    form.cleaned_data['nome'], 
                    form.cleaned_data['sobrenome'], 
                    form.cleaned_data['perfil'])
                return redirect("/")
        else:
            form = FormUtilizadores()
        return render(request, 'utilizadores/registar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)

def utilizadores_atualizar(request, id):
    try:
        if request.method == 'POST':
            form = FormUtilizadores(request.POST)
            if form.is_valid():
                create_utilizador(id,
                    form.cleaned_data['email'], 
                    form.cleaned_data['nome'], 
                    form.cleaned_data['sobrenome'], 
                    form.cleaned_data['perfil'])
                return redirect("/")
        else:
            form = FormUtilizadores()
            utilizador = readone_utilizador(id)
            print(utilizador)
            form.preencher_form({
                'email': utilizador['email'],
                'nome': utilizador['nome'],
                'sobrenome': utilizador['sobrenome'],
                'perfil': utilizador['perfil']
            })
        return render(request, 'utilizadores/atualizar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)