from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    
    # Componentes
    path('componentes/listar', views.componentes_listar, name='componentes_listar'),
    path('componentes/registar', views.componentes_registar, name='componentes_registar'),
    path('componentes/atualizar/<int:id>', views.componentes_atualizar, name='componentes_atualizar'),
    
    # Clientes
    path('clientes/listar', views.clientes_listar, name='clientes_listar'),
    path('clientes/registar', views.clientes_registar, name='clientes_registar'),
    path('clientes/atualizar/<int:id>', views.clientes_atualizar, name='clientes_atualizar'),

    # Fornecedores
    path('fornecedores/listar', views.fornecedores_listar, name='fornecedores_listar'),
    path('fornecedores/registar', views.fornecedores_registar, name='fornecedores_registar'),
    path('fornecedores/atualizar/<int:id>', views.fornecedores_atualizar, name='fornecedores_atualizar'),

    # Utilizadores
    path('utilizadores/listar', views.utilizadores_listar, name='utilizadores_listar'),
    path('utilizadores/listar/id/<int:id>', views.utilizadores_listar_id, name='utilizadores_listar_id'),
    path('utilizadores/registar', views.utilizadores_registar, name='utilizadores_registar'),
    path('utilizadores/iniciar-sessao', views.utilizadores_iniciar_sessao, name='utilizadores_iniciar_sessao'),
    path('utilizadores/atualizar/<int:id>', views.utilizadores_atualizar, name='utilizadores_atualizar'),

    # Equipamentos
    path('equipamentos/listar', views.equipamentos_listar, name='equipamentos_listar'),
    path('equipamentos/registar', views.equipamentos_registar, name='equipamentos_registar'),
    #path('equipamentos/atualizar/<int:id>', views.equipamentos_atualizar, name='equipamentos_atualizar'),
    
    # Ficha Producao, Componentes, Equipamento...
    path('fichaproducao/listar', views.fichaproducoes_listar, name='fichaproducoes_listar'),
    path('fichaproducao/listar/id/<int:id>', views.fichaproducoes_listar_id, name='fichaproducoes_listar_id'),
    path('fichaproducao/registar', views.fichaproducoes_registar, name='fichaproducoes_registar'),
    path('fichaproducao/atualizar/<int:id>', views.fichaproducoes_atualizar, name='fichaproducoes_atualizar'),
    
    # Encomendas, Remessas, Faturas...
    path('compras/listar', views.compras_historico_listar, name='historico_compras_listar'),
    #path('compras/registar', views.compras_historico_listar, name='historico_compras_listar'),
    #path('compras/atualizar/<int:id>', views.compras_historico_listar, name='historico_compras_listar'),
    
    # Encomendas, Remessas, Faturas...
    #path('vendas/listar', views.vendas_listar, name='vendas_listar'),
    #path('vendas/registar', views.vendas_registar, name='vendas_registar'),
    #path('vendas/atualizar/<int:id>', views.vendas_atualizar, name='vendas_atualizar'),
    
    # Utilizadores, Clientes, Fornecedores
    #path('colaboradores/listar', views.colaboradores_listar, name='colaboradores_listar'),
    #path('colaboradores/registar', views.colaboradores_registar, name='colaboradores_registar'),
    #path('colaboradores/atualizar/<int:id>', views.colaboradores_atualizar, name='colaboradores_atualizar'),
]