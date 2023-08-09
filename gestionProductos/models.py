from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=200, unique=True)
    marca_producto = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen_producto = models.ImageField(upload_to='productos/imagen_producto', blank=True, null=True)

    def __str__(self):
        return self.nombre_producto

class Cliente (models.Model):
    nombre_cliente = models.CharField(max_length=50)
    cedula_cliente = models.CharField(max_length=10)
    direccion_cliente = models.CharField(max_length=250) 
    telefono_cliente = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_cliente


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_venta = models.DateField("Fecha de venta", auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"Venta de {self.cantidad} unidades de '{self.producto}' a '{self.cliente}'"


