from django.urls import path

from . import views 
from .views import atualizar_componentes, listar_componentes


urlpatterns = [
    # path('', pagina_inicial, name='pagina_inicial'),
    path('/atualizar_componentes', atualizar_componentes, name='atualizar_componentes'),
    path('listar_componentes/', listar_componentes, name='listar_componentes'),
 ]