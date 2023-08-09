from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from PIL import Image



from gestionProductos.models import Producto
# Create your views here.

def inicio(request):
    productoListado = Producto.objects.all()
    return render(request, 'listar_productos.html', {'producto':productoListado})

def registrarProducto(request):
    nombre_producto = request.POST['nombre_producto']
    marca_producto = request.POST['marca_producto']
    precio = request.POST['precio']
    
    imagen_producto = request.FILES.get('imagen_producto')    
    
    producto = Producto.objects.create(nombre_producto=nombre_producto, marca_producto=marca_producto, precio=precio)    
    
    if imagen_producto:
        producto.imagen_producto = imagen_producto
    producto.save()    
    
    return redirect ('/')

def editarProducto(request, id):
    producto = Producto.objects.get(id = id)
    return render(request, 'editar_productos.html', {'producto': producto})

def actualizarProducto(request):
    id = request.POST['id']
    nombre_producto = request.POST['nombre_producto']
    marca_producto = request.POST['marca_producto']
    precio = request.POST['precio']    
    
    producto = Producto.objects.get(id = id)    
    
    producto.nombre_producto = nombre_producto
    producto.marca_producto = marca_producto
    producto.precio = precio
    
    if 'imagen_producto' in request.FILES:
        producto.imagen_producto = request.FILES['imagen_producto']
    producto.save()
    return redirect('/')

def eliminarProducto (request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect('/')