from django.contrib import admin
from .models import Producto, Cliente, Venta

# Register your models here.



class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'marca_producto', 'precio', 'imagen')

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'cedula_cliente', 'direccion_cliente', 'telefono_cliente')

class VentasAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'producto', 'cantidad', 'fecha_venta')

admin.site.register (Producto, ProductosAdmin)
admin.site.register (Cliente, ClientesAdmin)
admin.site.register (Venta, VentasAdmin)
