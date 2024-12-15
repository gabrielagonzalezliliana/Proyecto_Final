from django.db import models

# Create your models here.
class socios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

class actividades(models.Model):
    nombre = models.CharField(max_length=30)
    horario = models.TimeField()
    profesor = models.CharField(max_length=50)
    descripcion = models.TextField()


class sucursales(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

