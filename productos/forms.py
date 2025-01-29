from django import forms
from .models import Producto

# clase 19, Formularios
class FormularioProducto(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    descripcion = forms.CharField(label='Descripcion', max_length=300)
    precio = forms.DecimalField(label='Precio', max_digits=10, decimal_places=2)
    disponible = forms.BooleanField(label='Disponible', initial=True, required=False)
    foto = forms.ImageField(label='Foto', required=False)

    def guardar(self):
        Producto.objects.create(
            nombre=self.cleaned_data['nombre'],
            descripcion=self.cleaned_data['descripcion'],
            precio=self.cleaned_data['precio'],
            disponible=self.cleaned_data['disponible'],
            foto=self.cleaned_data['foto']
        )
