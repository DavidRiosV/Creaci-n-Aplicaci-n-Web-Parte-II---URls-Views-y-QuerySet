# urls.py
from django.urls import path, re_path
from . import views  # Asegúrate de importar views

urlpatterns = [
    path('', views.index, name='index_html'),  # Página de inicio
    re_path(r'^perfil/(?P<alias>[a-zA-Z0-9_-]+)/$', views.listar_perfil, name='listar_perfil'), 
    path('juegos/', views.listar_juegos, name='listar_juegos'), 
    path('amigos/<int:usuario_id>/', views.listar_amigos, name='listar_amigos')
]
