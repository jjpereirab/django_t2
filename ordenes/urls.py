from django.urls import path
from .views import VistaMiOrden, VistaCrearProductoEnOrden

urlpatterns = [
    path('mi_orden/', VistaMiOrden.as_view(), name='orden-list'),
    path('agregar_producto/', VistaCrearProductoEnOrden.as_view(), name='orden-add-product'),
]