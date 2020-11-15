from django.db import models

# Create your models here.


class Pedido(models.Model):
    fecha = models.DateField()
    estado = models.BooleanField()
    
class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()
    pedido = models.ManyToManyField(Pedido)
    id = models.IntegerField(primary_key=True)
    #pedido Pedido
    