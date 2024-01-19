from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.experimentos, name='experimentos'),
    path('componentes/listar', views.componentes_listar, name='componentes_listar'),
    path('componentes/registrar', views.componentes_registrar, name='componentes_registrar'),
    path('componentes/atualizar', views.componentes_atualizar, name='componentes_atualizar'),
    path('compras/listar', views.compras_historico_listar, name='historico_compras_listar'),
    path('equipamento/listar', views.equipamentos_listar, name='equipamentos_listar'),
    path('equipamento/registar', views.equipamento_registar, name='equipamento_registar'),
]