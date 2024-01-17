from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.experimentos, name='experimentos'),
    path('componentes/listar', views.componentes_listar, name='componentes_listar'),
    path('componentes/registrar', views.componentes_registrar, name='componentes_registrar'),
    path('componentes/atualizar', views.componentes_atualizar, name='componentes_atualizar'),
]