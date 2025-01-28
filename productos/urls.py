from django.urls import path
from .views import vista_producto


urlpatterns = [ # todas estas urls llevan /productos/ al inicio
    path('<int:id>', vista_producto),
]