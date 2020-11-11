from django.contrib import admin
from poleras.models import Producto,Pedido

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio',]
    search_fields = ['nombre']

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Pedido)