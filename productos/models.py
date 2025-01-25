from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.TextField(max_length=100, verbose_name="nombre")
    descripcion = models.TextField(max_length=300, verbose_name="descripcion")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    disponible = models.BooleanField(default=True, verbose_name="disponible")
    foto = models.ImageField(upload_to="logos", null=True, blank=True, verbose_name="foto")

    def __str__(self):
        return self.nombre