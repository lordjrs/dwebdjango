from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=9)
    contraseña = models.CharField(max_length=30)
    correo = models.EmailField(max_length=60)


class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()

class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    estado= models.BooleanField()
    
    