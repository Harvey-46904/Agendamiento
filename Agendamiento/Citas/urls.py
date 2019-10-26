from django.urls import path
from .views import *
urlpatterns = [
  path('crear_genero/',CrearGenero,name ='Crear_Genero'),
  path('listar_genero',ListarGenero,name='listar_autor')
]