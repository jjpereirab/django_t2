from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto

# Create your models here.
class Orden(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # si se borra el usuario, se borra la orden
    activa = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True, verbose_name="creacion")

    def __str__(self):
        return f"Orden {self.id} por usuario {self.usuario}"
    
class ProductoEnOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE) # si se borra la orden, se borra el ProductoEnOrden
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT) # si se borra el producto, proteger el ProductoEnOrden
    cantidad = models.IntegerField()

    def __str__(self):
        return f"orden: {self.orden} - producto: {self.producto}"
    
