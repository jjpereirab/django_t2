from django.forms import ModelForm
from .models import ProductoEnOrden

class FormularioProductoEnOrden(ModelForm):
    class Meta:
        model = ProductoEnOrden
        fields = ['producto']