from django.shortcuts import render
from .models import Componente

def listar_componentes(request):
    componentes = Componente.objects.all()
    return render(request, 'templates/componentes/listar.html', {'componentes': componentes})

def atualizar_componentes(request):
    componentes = Componente.objects.all()
    return render(request, 'templates/componentes/atualizar.html', {'componentes': componentes})


# Create your views here.
