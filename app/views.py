from django.shortcuts import render
from django.http import HttpResponse
from .database.detalhe_encomenda_fornecedor import fn_read_detalhe_encomenda_fornecedor
import logging

logger = logging.getLogger(__name__)

def experimentos(request):
    try:
        detalhes_encomenda = fn_read_detalhe_encomenda_fornecedor()
        if detalhes_encomenda:
            logger.info("Detalhes da Encomenda do Fornecedor: %s", detalhes_encomenda)
        else:
            print("Não há detalhes de encomenda para fornecedor disponíveis.")

        return render(request, 'componentes/componentes_encomenda.html', {'detalhes_encomenda': detalhes_encomenda})
        
    except Exception as e:
        print("fodeu")
        return HttpResponse(e)