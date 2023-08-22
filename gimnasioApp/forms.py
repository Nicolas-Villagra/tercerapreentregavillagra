from django import forms

class CursosForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    categoria=forms.CharField(max_length=30)
    turno=forms.CharField(max_length=10)

class ProfesorForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    profesion= forms.CharField(max_length=30)
    email= forms.EmailField(max_length=30)

class RutinasForm(forms.Form):
    rutina= forms.CharField(max_length=40)
    nivel= forms.CharField(max_length=40)


class ClientesForms(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    celular=forms.IntegerField()
    direccion=forms.CharField(max_length=50)


class SuplementosForm(forms.Form):
    marca=forms.CharField(max_length=30)
    origen=forms.CharField(max_length=30)