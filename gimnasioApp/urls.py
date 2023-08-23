from django.urls import path
from .views import *



urlpatterns = [
    
  
   path("curso/", curso, name="curso"),
   path("profesor/", profesor, name="profesor"),
   path("rutina/", rutina, name="rutina"),
   path("cliente/", cliente, name="cliente"),
   path("suplemento/", suplemento, name="suplementos"),

   path("eliminarCurso/<id>", eliminarCurso, name="eliminarCurso"),
   path("editarCurso/<id>", editarCurso, name="editarCurso"),
   path("eliminarProfesor/<id>", eliminarProfesor, name="eliminarProfesor"),
   path("editarProfesor/<id>", editarProfesor, name="editarProfesor"),
   path("eliminarRutina/<id>", eliminarRutina, name="eliminarRutina"),
   path("editarRutina/<id>", editarRutina, name ="editarRutina"),
   path("eliminarSuplemento/<id>", eliminarSuplemento, name="eliminarSuplemento"),
   path("editarSuplemento/<id>",editarSuplemento, name="editarSuplemento"),
   path("eliminarCliente/<id>", eliminarCliente, name="eliminarCliente"),
   path("editarCliente/<id>", editarCliente, name="editarCliente"),
 
   
]
  