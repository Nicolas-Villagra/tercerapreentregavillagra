from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *

def inicio(request):
    return render(request,"gimnasioApp/inicio.html")


def curso(request):
    if request.method=="POST":
        form=CursosForm(request.POST) 
        if  form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            categoria=info["categoria"]
            turno=info["turno"]
            curso = cursos (nombre=nombre,categoria=categoria,turno=turno)
            curso.save()
            formulario_curso=CursosForm
            return render(request,"gimnasioApp/curso.html", {"mensaje":"Creado Exitosamente", "formulario":formulario_curso})
        else:
            return render(request,"gimnasioApp/curso.html", {"mensaje":"Datos Invalidos", "formulario":formulario_curso })
    else:
        formulario_curso=CursosForm()
        return render(request,"gimnasioApp/curso.html", {"formulario":formulario_curso})


def profesor(request):
    if request.method=="POST":
        form=ProfesorForm(request.POST)
        if form.is_valid():
           info=form.cleaned_data
           nombre=info ["nombre"]
           apellido=info ["apellido"]
           profesion=info ["profesion"]
           email=info ["email"]
           profesor = profesores (nombre=nombre, apellido=apellido, profesion=profesion, email=email)
           profesor.save()
           formulario_profesor=ProfesorForm()
           return render(request, "gimnasioApp/profesor.html", {"mensaje":"Instructor Cargado", "formulario":formulario_profesor})
        else:
           return render (request, "gimnasioApp/profesor.html", {"mensaje":"Datos Invalidos", "formulario":formulario_profesor}) 
    else:
        formulario_profesor=ProfesorForm()
        return render(request, "gimnasioApp/profesor.html", {"formulario": formulario_profesor})
    



def rutina(request):
    if request.method=="POST":
        form=RutinasForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            rutina=info["rutina"]
            nivel=info["nivel"]
            rutina=rutinas(rutina=rutina, nivel=nivel)
            rutina.save()
            formulario_rutina=RutinasForm()
            return render (request, "gimnasioApp/rutina.html", {"mensaje": "Rutina Cargada","formulario": formulario_rutina})
        else:
           return render (request, "gimnasioApp/rutina.html", {"mensaje": "Datos Invalidos","formulario": formulario_rutina}) 
    else:
        formulario_rutina=RutinasForm()
        return render (request, "gimnasioApp/rutina.html", {"formulario": formulario_rutina})


def cliente(request):
    if request.method=="POST":
        form=ClientesForms(request.POST)
        if form.is_valid():
           info=form.cleaned_data
           nombre=info["nombre"]
           apellido=info["apellido"]
           celular=info["celular"]
           direccion=["direccion"]
           cliente= clientes (nombre=nombre, apellido=apellido, celular=celular, direccion=direccion)
           cliente.save()
           formulario_cliente=ClientesForms()
           return render (request, "gimnasioApp/cliente.html", {"mensaje":"Cargado", "formulario": formulario_cliente})
        else:
            return render (request, "gimnasioApp/cliente.html",{"mensaje":"Invalido", "formulario": formulario_cliente})
    else:
        formulario_cliente=ClientesForms()
        return render (request, "gimnasioApp/cliente.html", {"mensaje": formulario_cliente})
        


def suplemento(request):
    if request.method=="POST":
        form=SuplementosForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            marca=form["marca"]
            origen=form["origen"]
            suplemento= suplementos (marca=marca, origen=origen)
            suplemento.save()
            formulario_suplemento=SuplementosForm()
            return render (request, "gimnasioApp/suplementos.html", {"mensaje":"Carga Exitosa", "formulario": formulario_suplemento})
        else:
            return render (request, "gimnasioApp/suplementos.html", {"mensaje": "Datos Invalidos","formulario": formulario_suplemento})
    else:
        formulario_suplemento=SuplementosForm()
        return render (request, "gimnasioApp/suplementos.html",{"formulario": formulario_suplemento})