from rest_framework.serializers import ModelSerializer
from .models import Producto

class SerializerDeProducto(ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            "id",
            "nombre",
            "descripcion",
            "precio",
            "disponible",
            "foto",
            "creacion",
        ]