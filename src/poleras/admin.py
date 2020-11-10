from django.contrib import admin
from poleras.models import Cliente,Producto,Pedido

# Register your models here.

# Manipular bd como user admin
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)

