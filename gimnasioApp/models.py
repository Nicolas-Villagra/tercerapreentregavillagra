from django.db import models

# Create your models here.
class cursos(models.Model):
    nombre=models.CharField(max_length=20)
    categoria=models.CharField(max_length=20)
    turno=models.CharField(max_length=10)
    def __str__(self):
        return f"{self.nombre} - {self.categoria}"

class profesores(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    profesion= models.CharField(max_length=20)
    email= models.EmailField()
    def __str__(self):
        return f"{self.nombre} - {self.profesion}"


class rutinas(models.Model):
    rutina= models.CharField(max_length=20)
    nivel= models.CharField(max_length=20)
    def __str__(self):
        return f"{self.rutina}"


class clientes(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    celular=models.IntegerField()
    direccion=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} - {self.apellido} {self.direccion}"
    
class suplementos(models.Model):
    marca=models.CharField(max_length=30)
    origen=models.CharField(max_length=30)
    def __str__(self):
        return f"{self.marca}"
