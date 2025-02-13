from rest_framework import serializers
from .models import Orden, ProductoEnOrden


class SerializadorProductoEnOrden(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source="producto.nombre", read_only=True)  # Muestra el nombre del producto

    class Meta:
        model = ProductoEnOrden
        fields = ["id", "producto", "producto_nombre", "cantidad"]


class SerializadorOrden(serializers.ModelSerializer):
    productos = SerializadorProductoEnOrden(source="productoenorden_set", many=True, read_only=True)
    usuario_username = serializers.CharField(source="usuario.username", read_only=True)  # Muestra el username del usuario

    class Meta:
        model = Orden
        fields = ["id", "usuario", "usuario_username", "activa", "creacion", "productos"]


class SerializadorCrearOrden(serializers.ModelSerializer):
    productos = SerializadorProductoEnOrden(source="productoenorden_set", many=True)  # Permite enviar productos en la creación

    class Meta:
        model = Orden
        fields = ["id", "usuario", "activa", "productos"]

    def create(self, validated_data):
        productos_data = validated_data.pop("productoenorden_set")  # Extrae los productos del request
        orden = Orden.objects.create(**validated_data)  # Crea la orden

        for producto_data in productos_data:
            ProductoEnOrden.objects.create(orden=orden, **producto_data)  # Crea cada producto en la orden

        return orden        