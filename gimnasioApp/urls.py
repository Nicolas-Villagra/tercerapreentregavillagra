from django.urls import path
from .views import *



urlpatterns = [
    
  
   path("curso/", curso, name="curso"),
   path("profesor/", profesor, name="profesor"),
   path("rutina/", rutina, name="rutina"),
   path("cliente/", cliente, name="cliente"),
   path("suplemento/", suplemento, name="suplementos"),
   path("busquedaCliente/", busquedaCliente, name="busquedaCliente"),
   path("buscar/", buscar, name="buscar"),
]
  