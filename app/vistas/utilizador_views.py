from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..utils import *
from ..database.utilizador import *
from ..forms import *

def utilizadores_listar(request):
    try:
        utilizadores = readjson_utilizador()
        return render(request, 'utilizadores/listar.html', {'utilizadores': utilizadores})
    except Exception as e:
        return HttpResponse(e)

def utilizadores_listar_id(request, id):
    try:
        utilizador = readone_utilizador(id)
        return render(request, 'utilizadores/listar_id.html', {'utilizador': utilizador})
    except Exception as e:
        return HttpResponse(e)

def utilizadores_iniciar_sessao(request):
    try:
        if request.method == 'POST':
            form = FormUtilizadoresIniciarSessao(request.POST)
            if form.is_valid():
                form_email = form.cleaned_data['email']
                form_senha = form.cleaned_data['senha']
                user = login_utilizador(form_email, form_senha)
                user = stringToArray(user[0])
                if user[0] == 't':
                    id = user[1]
                    nome = user[2]
                    sobrenome = user[3]
                    email = user[4]
                    perfil = user[5]
                    print(id, nome, sobrenome, email, perfil)
                    return render(request, 'add_user.html', {'id': id, 'nome': nome, 'sobrenome': sobrenome, 'email': email, 'perfil': perfil})
                else:
                    # apresenta aviso
                    return
        else:
            form = FormUtilizadoresIniciarSessao()
        return render(request, 'utilizadores/iniciar_sessao.html', {'form': form})

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
                update_utilizador(id,
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
                'perfil': utilizador['perfil_id']
            })
        return render(request, 'utilizadores/atualizar.html', {'form': form})

    except Exception as e:
        return HttpResponse(e)