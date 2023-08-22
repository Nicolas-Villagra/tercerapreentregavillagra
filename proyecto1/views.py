from django.http import HttpResponse
from django.template import Template, context, loader

def saludo(request):
    return HttpResponse ("hola")

def saludo_dos(request):
    return HttpResponse ("hola x 2")

def mostrandohtml(request):
    dicc={"nombre":"Nicolas","apellido":"Villagra","lista_notas":[1,2,3,4,5,6] }

    template=loader.get_template("template.html")
    documento=template.render(dicc)
    return HttpResponse(documento)