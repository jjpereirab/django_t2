from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Producto
from django.views import generic
from .forms import FormularioProducto

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
    # success_url = reverse_lazy('url_name_agregar_producto') # <--- SE TIENE QUE LLAMAR success_url
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

class VistaListaProductosTabla(generic.ListView):
    model = Producto  # Specify the model
    template_name = 'productos/lista_productos_tabla.html'
    context_object_name = 'items'