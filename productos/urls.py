from django.urls import path
from .views import vista_producto, VistaFormularioProducto, VistaListaProductos, lista_productos


urlpatterns = [ # todas estas urls llevan /productos/ al inicio
    path('<int:id>', vista_producto),
    path('agregar', VistaFormularioProducto.as_view(), name='url_name_agregar_producto'), # clase 19, Formularios    
]
