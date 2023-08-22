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
        curso=cursos.objects.all()
        return render(request,"gimnasioApp/curso.html", {"formulario":formulario_curso, "curso":cursos})


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
           mensaje="Instructor Cargado"
           
        else:
           mensaje="No se pudo Cargar"

        formulario_profesor=ProfesorForm()
        return render (request, "gimnasioApp/profesor.html", {"mensaje":mensaje, "formulario":formulario_profesor}) 
    else:
        formulario_profesor=ProfesorForm()
        profesor=profesores.objects.all()
    return render(request, "gimnasioApp/profesor.html", {"formulario": formulario_profesor, "profesor": profesores})
    



def rutina(request):
    if request.method=="POST":
        form=RutinasForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            rutina=info["rutina"]
            nivel=info["nivel"]
            rutina=rutinas(rutina=rutina, nivel=nivel)
            rutina.save()
            mensaje="Rutina Cargada"
            
        else:
           mensaje="No se pudo cargar"

        formulario_rutina=RutinasForm()
        return render (request, "gimnasioApp/rutina.html", {"mensaje":mensaje,"formulario": formulario_rutina}) 
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
           mensaje="Creado Correctamente"
          
        else:
            mensaje="Datos Incorrectos"

        formulario_clientes=ClientesForms()
        return render (request,"gimnasioApp/cliente.html", {"mensaje":mensaje,"formulario": formulario_clientes})
    else:
        formulario_clientes=ClientesForms()
    cliente=clientes.objects.all()
    return render (request, "gimnasioApp/cliente.html", {"mensaje": formulario_clientes, "cliente": clientes})
        


def suplemento(request):
    if request.method=="POST":
        form=SuplementosForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            marca=form["marca"]
            origen=form["origen"]
            suplemento= suplementos (marca=marca, origen=origen)
            suplemento.save()
            mensaje="Cargado"
            
        else:
            mensaje=" No se pudo cargar"

        formulario_suplemento=SuplementosForm()
        return render (request, "gimnasioApp/suplementos.html", {"mensaje":mensaje,"formulario": formulario_suplemento})
    else:
        formulario_suplemento=SuplementosForm()

    suplemento=suplementos.objects.all()
    return render (request, "gimnasioApp/suplementos.html",{"formulario": formulario_suplemento, "suplemento":suplementos})



#def listar_suplemento(request):
#    Suplemento=suplemento.objects.all()
#    respuesta=""
 #   for Suplemento in suplemento:
  #      respuesta+=f" {Suplemento.marca} - {Suplemento.origen}"