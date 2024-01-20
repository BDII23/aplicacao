from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    
    # Componentes
    path('componentes/listar', views.componentes_listar, name='componentes_listar'),
    path('componentes/registrar', views.componentes_registrar, name='componentes_registrar'),
    path('componentes/atualizar/<int:id>', views.componentes_atualizar, name='componentes_atualizar'),
    path('componentes/apagar/<int:id>', views.componentes_apagar, name='componentes_apagar'),
    
    # Equipamentos
    path('equipamento/listar', views.equipamentos_listar, name='equipamentos_listar'),
    path('equipamento/registar', views.equipamento_registar, name='equipamento_registar'),
    #path('equipamento/atualizar/<int:id>', views.equipamento_atualizar, name='equipamento_atualizar'),
    
    # Ficha Producao, Componentes, Equipamento...
    #path('fichaproducao/listar', views.fichaproducaos_listar, name='fichaproducaos_listar'),
    #path('fichaproducao/registar', views.fichaproducao_registar, name='fichaproducao_registar'),
    #path('fichaproducao/atualizar', views.fichaproducao_atualizar, name='fichaproducao_atualizar'),
    
    # Encomendas, Remessas, Faturas...
    path('compras/listar', views.compras_historico_listar, name='historico_compras_listar'),
    #path('compras/registrar', views.compras_historico_listar, name='historico_compras_listar'),
    #path('compras/atualizar', views.compras_historico_listar, name='historico_compras_listar'),
    
    # Encomendas, Remessas, Faturas...
    #path('vendas/listar', views.vendas_listar, name='vendas_listar'),
    #path('vendas/registrar', views.vendas_registrar, name='vendas_registrar'),
    #path('vendas/atualizar', views.vendas_atualizar, name='vendas_atualizar'),
    
    # Utilizadores, Clientes, Fornecedores
    #path('colaboradores/listar', views.colaboradores_listar, name='colaboradores_listar'),
    #path('colaboradores/registrar', views.colaboradores_registrar, name='colaboradores_registrar'),
    #path('colaboradores/atualizar', views.colaboradores_atualizar, name='colaboradores_atualizar'),
]