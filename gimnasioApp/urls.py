from django.urls import path
from .views import *



urlpatterns = [
    
  
   path("curso/", curso, name="curso"),
   path("profesor/", profesor, name="profesor"),
   path("rutina/", rutina, name="rutina"),
   path("cliente/", cliente, name="cliente"),
   path("suplementos/", suplemento, name="suplementos"),
   path("busquedaCliente/", busquedaCliente, name="busquedaCliente"),
   path("buscar/", buscar, name="buscar"),
]
  