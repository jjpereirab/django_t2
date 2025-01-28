from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.
def vista_producto(request, *args, **kwargs):
    print(args)
    print(kwargs)
    product = Producto.objects.get(id=kwargs['id'])
    return HttpResponse(f"Producto: {product.nombre} \nDescripcion: {product.descripcion} \nPrecio: {product.precio} \nDisponible: {product.disponible} \nFoto: {product.foto}")
