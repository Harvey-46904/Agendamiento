from django.urls import path
from .views import CrearGenero
urlpatterns = [
  path('crear_genero/',CrearGenero,name ='Crear_Genero')
]