from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Producto
from .forms import FormularioProducto
from .serializers import SerializerDeProducto

# vista para reto de clase 18
def vista_producto(request, *args, **kwargs):
    print(args)
    print(kwargs)
    product = Producto.objects.get(id=kwargs['id'])
    return HttpResponse(f"Producto: {product.nombre} \nDescripcion: {product.descripcion} \nPrecio: {product.precio} \nDisponible: {product.disponible} \nFoto: {product.foto}")

# clase 19, Formularios
class VistaFormularioProducto(generic.FormView):
    template_name = "productos/agregar_producto.html"   # <--- SE TIENE QUE LLAMAR template_name
    form_class = FormularioProducto                     # <--- SE TIENE QUE LLAMAR form_class
    success_url = reverse_lazy('url_name_lista_productos_cbv') # <--- SE TIENE QUE LLAMAR success_url, **tarea**

    def form_valid(self, form):
        form.guardar()
        return super().form_valid(form)

# clase 19, tarea
# ---------------
# forma 1
class VistaListaProductos(generic.ListView):
    model = Producto  
    template_name = 'productos/lista_productos.html'
    context_object_name = 'items'  

# forma 2
from django.shortcuts import render
def lista_productos(request):
    items = Producto.objects.all()  
    return render(request, 'productos/lista_productos.html', {'items': items})

# Esta es la buena
class VistaListaProductosTabla(generic.ListView):
    model = Producto  # Specify the model
    template_name = 'productos/lista_productos_tabla.html'
    context_object_name = 'items'

# clase 27
class VistaListaProductoAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        productos = Producto.objects.all()
        serializador = SerializerDeProducto(productos, many=True)
        return Response(serializador.data)
    

# tarea clase 27 - vista para CRUD de Producto
from rest_framework import viewsets
class ProductoAPI(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
        
    queryset = Producto.objects.all()
    serializer_class = SerializerDeProducto