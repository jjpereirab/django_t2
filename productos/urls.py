from django.urls import path
from .views import vista_producto, VistaFormularioProducto, VistaListaProductos, lista_productos, VistaListaProductosTabla


urlpatterns = [ # todas estas urls llevan /productos/ al inicio
    # clase 18, tarea
    path('<int:id>', vista_producto),
    # clase 19, Formularios
    path('agregar', VistaFormularioProducto.as_view(), name='url_name_agregar_producto'), 
    # clase 19, tarea
    path('lista_cbv', VistaListaProductos.as_view(), name='url_name_lista_productos_cbv'),  # forma 1
    path('lista_fbv', lista_productos, name='url_name_lista_productos_fbv'),                # forma 2
    path('lista_cbv_tabla', VistaListaProductosTabla.as_view(), name='url_name_lista_productos_cbv_tabla'),  
]
