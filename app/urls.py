from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    
    # Componentes
    path('componentes/listar', views.componentes_listar, name='componentes_listar'),
    path('componentes/registar', views.componentes_registar, name='componentes_registar'),
    path('componentes/atualizar/<int:id>', views.componentes_atualizar, name='componentes_atualizar'),
    
    # Equipamentos
    path('equipamento/listar', views.equipamentos_listar, name='equipamentos_listar'),
    path('equipamento/registar', views.equipamento_registar, name='equipamento_registar'),
    #path('equipamento/atualizar/<int:id>', views.equipamento_atualizar, name='equipamento_atualizar'),
    
    # Ficha Producao, Componentes, Equipamento...
    path('fichaproducao/listar', views.fichaproducoes_listar, name='fichaproducoes_listar'),
    path('fichaproducao/registar', views.fichaproducoes_registar, name='fichaproducoes_registar'),
    path('fichaproducao/atualizar', views.fichaproducoes_atualizar, name='fichaproducoes_atualizar'),
    
    # Encomendas, Remessas, Faturas...
    path('compras/listar', views.compras_historico_listar, name='historico_compras_listar'),
    #path('compras/registar', views.compras_historico_listar, name='historico_compras_listar'),
    #path('compras/atualizar', views.compras_historico_listar, name='historico_compras_listar'),
    
    # Encomendas, Remessas, Faturas...
    #path('vendas/listar', views.vendas_listar, name='vendas_listar'),
    #path('vendas/registar', views.vendas_registar, name='vendas_registar'),
    #path('vendas/atualizar', views.vendas_atualizar, name='vendas_atualizar'),
    
    # Utilizadores, Clientes, Fornecedores
    #path('colaboradores/listar', views.colaboradores_listar, name='colaboradores_listar'),
    #path('colaboradores/registar', views.colaboradores_registar, name='colaboradores_registar'),
    #path('colaboradores/atualizar', views.colaboradores_atualizar, name='colaboradores_atualizar'),
]