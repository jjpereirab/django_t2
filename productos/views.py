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
    success_url = reverse_lazy('url_name_agregar_producto') # <--- SE TIENE QUE LLAMAR success_url

    def form_valid(self, form):
        form.guardar()
        return super().form_valid(form)

