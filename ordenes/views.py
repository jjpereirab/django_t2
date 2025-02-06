from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Orden


# Create your views here.
class VistaMiOrden(LoginRequiredMixin, DetailView):
    model = Orden # <---- se tiene que llamar 'model', ver https://ccbv.co.uk/projects/Django/5.0/django.views.generic.detail/DetailView/
    template_name = "ordenes/mi_orden.html"
    context_object_name = "ordencilla" # <---- vinculo con el template

    def get_object(self, queryset=None):
        return Orden.objects.filter(activa=True, usuario=self.request.user).first()
        # return Orden.objects.filter(activa=True).first()