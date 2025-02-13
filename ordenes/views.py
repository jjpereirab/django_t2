from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Orden
from .forms import FormularioProductoEnOrden
from django.urls import reverse_lazy

# Create your views here.
class VistaMiOrden(LoginRequiredMixin, DetailView):
    model = Orden # <---- se tiene que llamar 'model', ver https://ccbv.co.uk/projects/Django/5.0/django.views.generic.detail/DetailView/
    template_name = "ordenes/mi_orden.html"
    context_object_name = "ordencilla" # <---- vinculo con el template

    def get_object(self, queryset=None):
        return Orden.objects.filter(activa=True, usuario=self.request.user).first()
        # return Orden.objects.filter(activa=True).first()

# clase 26
class VistaCrearProductoEnOrden(LoginRequiredMixin, CreateView):
    template_name = "ordenes/crear_producto_en_orden.html"
    form_class = FormularioProductoEnOrden
    success_url = reverse_lazy('orden-list')

    def form_valid(self, form): # ver https://ccbv.co.uk/projects/Django/5.0/django.views.generic.edit/CreateView/
        orden, creada = Orden.objects.get_or_create(activa=True, usuario=self.request.user, )
        form.instance.orden = orden
        form.instance.cantidad = 1
        form.save()
        return super().form_valid(form)
    

# clase 27 - tarea
from rest_framework.viewsets import ModelViewSet
from .models import Orden
from .serializers import SerializadorOrden, SerializadorCrearOrden

class OrdenAPI(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    
    queryset = Orden.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return SerializadorCrearOrden  # Usar el serializer con productos al crear
        return SerializadorOrden  # Usar el serializer normal para leer