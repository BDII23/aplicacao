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
    path('equipamentos/listar/id/<int:id>', views.equipamentos_listar_id, name='equipamentos_listar_id'),
    path('equipamentos/registar', views.equipamentos_registar, name='equipamentos_registar'),
    path('equipamentos/atualizar/<int:id>', views.equipamentos_atualizar, name='equipamentos_atualizar'),
    
    # Ficha Producao, Componentes, Equipamento...
    path('fichaproducao/listar', views.fichaproducoes_listar, name='fichaproducoes_listar'),
    path('fichaproducao/listar/id/<int:id>', views.fichaproducoes_listar_id, name='fichaproducoes_listar_id'),
    path('fichaproducao/registar', views.fichaproducoes_registar, name='fichaproducoes_registar'),
    path('fichaproducao/atualizar/<int:id>', views.fichaproducoes_atualizar, name='fichaproducoes_atualizar'),
    
    # Encomendas do Fornecedor
    path('fornecedor/encomendas/listar', views.fornecedores_encomendas_listar, name='fornecedores_encomendas_listar'),
    path('fornecedor/encomendas/listar/id/<int:id>', views.fornecedores_encomendas_listar_id, name='fornecedores_encomendas_listar_id'),
    path('fornecedor/encomendas/registar', views.fornecedores_encomendas_registar, name='fornecedores_encomendas_registar'),
    path('fornecedor/encomendas/atualizar/<int:id>', views.fornecedores_encomendas_atualizar, name='fornecedores_encomendas_atualizar'),

    # Remessas / Faturas do Fornecedor
    path('fornecedor/remessas/listar', views.fornecedores_remessas_listar, name='fornecedores_remessas_listar'),
    path('fornecedor/remessas/listar/id/<int:id>', views.fornecedores_remessas_listar_id, name='fornecedores_remessas_listar_id'),
    path('fornecedor/remessas/registar', views.fornecedores_remessas_registar, name='fornecedores_remessas_registar'),
    path('fornecedor/remessas/atualizar/<int:id>', views.fornecedores_remessas_atualizar, name='fornecedores_remessas_atualizar'),

    # Encomendas, Remessas, Faturas...
    path('compras/listar', views.compras_historico_listar, name='compras_listar'),
    #path('compras/registar', views.compras_historico_listar, name='compras_registrar'),
    #path('compras/atualizar/<int:id>', views.compras_historico_listar, name='compras_atualizar'),
    
    # Encomendas do Fornecedor
    path('clientes/encomendas/listar', views.clientes_encomendas_listar, name='clientes_encomendas_listar'),
    path('clientes/encomendas/listar/id/<int:id>', views.clientes_encomendas_listar_id, name='clientes_encomendas_listar_id'),
    path('clientes/encomendas/registar', views.clientes_encomendas_registar, name='clientes_encomendas_registar'),
    path('clientes/encomendas/atualizar/<int:id>', views.clientes_encomendas_atualizar, name='clientes_encomendas_atualizar'),

    # Remessas / Faturas do Fornecedor
    path('clientes/remessas/listar', views.clientes_remessas_listar, name='clientes_remessas_listar'),
    path('clientes/remessas/listar/id/<int:id>', views.clientes_remessas_listar_id, name='clientes_remessas_listar_id'),
    path('clientes/remessas/registar', views.clientes_remessas_registar, name='clientes_remessas_registar'),
    path('clientes/remessas/atualizar/<int:id>', views.clientes_remessas_atualizar, name='clientes_remessas_atualizar'),
]