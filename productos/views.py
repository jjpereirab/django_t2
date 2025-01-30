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
from django.views.generic import ListView
class VistaListaProductos(ListView):
    model = Producto  # Specify the model
    template_name = 'productos/lista_productos.html'  # Specify the template
    context_object_name = 'items'  # Name for the context variable

from django.shortcuts import render
def lista_productos(request):
    items = Producto.objects.all()  # Fetch all entries from the Item model
    return render(request, 'productos/lista_productos.html', {'items': items})
