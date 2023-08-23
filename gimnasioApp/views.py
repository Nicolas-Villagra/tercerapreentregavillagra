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
            mensaje="Creado"
            
        else:
            mensaje="Datos Invalidos"

        formulario_cursos=CursosForm()
        return render(request,"gimnasioApp/curso.html", {"mensaje":mensaje, "formulario":formulario_cursos})
    else:
       curso=cursos.objects.all()
    formulario_curso=CursosForm()
    return render(request,"gimnasioApp/curso.html", {"formulario":formulario_curso, "cursos":curso})


def eliminarCurso(request, id):
    curso = cursos.objects.get(id=id)
    curso.delete()
    curso = cursos.objects.all()
    formulario_curso=CursosForm()
    mensaje="Curso Eliminado"
    return render(request,"gimnasioApp/curso.html", {"mensaje": mensaje,"formulario":formulario_curso, "cursos":curso})


def editarCurso(request, id):
    curso = cursos.objects.get(id=id)
    if request.method=="POST":
        form=CursosForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            curso.nombre=info["nombre"]
            curso.categoria=info["categoria"]
            curso.turno=info["turno"]
            curso.save()
            mensaje="Curso Editado"
            curso=cursos.objects.all()
            formulario_curso= CursosForm()
            return render(request, "gimnasioApp/editarCurso.html", {"mensaje":mensaje, "formulario": formulario_curso, "cursos":curso})
    else:
        curso = cursos.objects.get(id=id)
        formulario_curso=CursosForm(initial={"nombre":curso.nombre,"categoria":curso.categoria,"turno":curso.turno})
        return render(request, "gimnasioApp/editarCurso.html",{"formulario":formulario_curso, "cursos":curso})
            

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
           mensaje="Profe Cargado"
           
        else:
           mensaje="No se pudo Cargar"

        formulario_profesor=ProfesorForm()
        return render (request, "gimnasioApp/profesor.html", {"mensaje":mensaje, "formulario":formulario_profesor}) 
    else:
        formulario_profesor=ProfesorForm()
    profesor=profesores.objects.all()
    return render(request, "gimnasioApp/profesor.html", {"formulario": formulario_profesor, "profesores": profesor})
    

def eliminarProfesor(request, id):
    profesor=profesores.objects.get(id=id)
    profesor.delete()
    profesor = profesores.objects.all()
    formulario_profesor=ProfesorForm()
    mensaje="Profe Eliminado"
    return render(request, "gimnasioApp/profesor.html", {"mensaje":mensaje, "formulario": formulario_profesor, "profesores": profesor})


def editarProfesor(request, id):
    profesor= profesores.objects.get(id=id)
    if request.method=="POST":
        form=ProfesorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            profesor.nombre = info["nombre"]
            profesor.apellido=info["apellido"]
            profesor.profesion= info["profesion"]
            profesor.email=info["email"]
            profesor.save()
            mensaje = "profe editado"
            profesor= profesores.objects.all()
            formulario_profesor=ProfesorForm()
            return render(request,"gimnasioApp/editarProfesor.html",{"mensaje":mensaje,"formulario":formulario_profesor,"profesores":profesor})
    else:
        profesor= profesores.objects.get(id=id)
        formulario_profesor=ProfesorForm(initial={"nombre":profesor.nombre,"apellido":profesor.apellido, "profesion": profesor.profesion,"email":profesor.email})
    return render(request,"gimnasioApp/editarProfesor.html",{"mensaje":mensaje,"formulario":formulario_profesor,"profesores":profesor})


    
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
    rutina=rutinas.objects.all()
    return render (request, "gimnasioApp/rutina.html", {"formulario": formulario_rutina, "rutinas":rutina})


def eliminarRutina(request, id):
    rutina=rutinas.objects.get(id=id)
    rutina.delete()
    rutina= rutinas.objects.all()
    formulario_rutina=RutinasForm()
    mensaje="Rutina Eliminada"
    return render (request, "gimnasioApp/rutina.html", {"mensaje":mensaje,"formulario": formulario_rutina, "rutinas":rutina})

def editarRutina(request, id):
    rutina= rutinas.objects.get(id=id)
    if request.method=="POST":
        form=RutinasForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            rutina.rutina=info["rutina"]
            rutina.nivel=info["nivel"]
            rutina.save()
            mensaje="Rutina Editada"
            rutina= rutinas.objects.all()
            formulario_rutina=RutinasForm()
            return render (request, "gimnasioApp/editarRutinas.html",{"mensaje":mensaje, "formulario": formulario_rutina, "rutinas":rutina})
    else:
        rutina= rutinas.objects.get(id=id)
        formulario_rutina=RutinasForm(initial={"rutina": rutina.rutina, "nivel": rutina.nivel})
        return render (request, "gimnasioApp/editarRutina.html",{"mensaje":mensaje,"formulario": formulario_rutina, "rutinas":rutina})




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
    return render (request, "gimnasioApp/cliente.html", {"formulario": formulario_clientes, "clientes": cliente})
        

def eliminarCliente(request, id):
    cliente=clientes.objects.get(id=id)
    cliente.delete()
    cliente= clientes.objects.all()
    formulario_clientes=ClientesForms()
    mensaje="Cliente Eliminado"
    return render (request, "gimnasioApp/cliente.html", {"mensaje": mensaje,"formulario": formulario_clientes, "clientes": cliente})
    
def editarCliente(request, id):
    cliente=clientes.objects.get(id=id)
    if request.method=="POST":
        form=ClientesForms(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            cliente.nombre=["nombre"]
            cliente.apellido=info["apellido"]
            cliente.celular=info["celular"]
            cliente.direccion=info["direccion"]
            cliente.save()
            mensaje="Cliente Editado"
            cliente=clientes.objects.all()
            formulario_cliente=ClientesForms()
            return render (request, "gimnasioApp/editarCliente.html",{"mensaje":mensaje,"formulario": formulario_cliente, "clientes":cliente})
    else:

        cliente=clientes.objects.get(id=id)
        formulario_cliente=ClientesForms(initial={"nombre":cliente.nombre,"apellido":cliente.apellido,"celular":cliente.celular,"direccion":cliente.direccion})
        return render(request, "gimnasioApp/editarCliente.html", {"formulario":formulario_cliente, "clientes":cliente})


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
    return render (request, "gimnasioApp/suplementos.html",{"formulario": formulario_suplemento, "suplementos":suplemento})

def eliminarSuplemento(request, id):
    suplemento=suplementos.objects.get(id=id)
    suplemento.delete()
    suplemento=suplementos.objects.all()
    formulario_suplemento=SuplementosForm()
    mensaje="Suplemento Eliminado"
    return render (request, "gimnasioApp/suplementos.html",{"mensaje":mensaje,"formulario": formulario_suplemento, "suplementos":suplemento})


def editarSuplemento(request, id):
    suplemento=suplementos.objects.get(id=id)
    if request.method=="POST":
        form=SuplementosForm(request.POST)
        info=form.cleaned_data
        suplemento.marca=info["marca"]
        suplemento.origen=info["origen"]
        suplemento.save()
        mensaje="Suplemento Editado"
        suplemento=suplementos.objects.all()
        formulario_suplemento=SuplementosForm()
        return render (request, "gimnasioApp/editarSuplemento.html",{"mensaje":mensaje, "formulario":formulario_suplemento, "suplementos":suplemento})
    else:

        suplemento=suplementos.objects.get(id=id)
        formulario_suplemento=SuplementosForm(initial={"nombre":suplemento.marca,"origen":suplemento.origen})
        return render (request, "gimnasioApp/editarSuplemento.html",{"formulario":formulario_suplemento, "suplementos": suplemento})