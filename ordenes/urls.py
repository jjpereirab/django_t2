from django.urls import path
from .views import VistaMiOrden

urlpatterns = [
    path('mi_orden/', VistaMiOrden.as_view(), name='orden-list'),
]