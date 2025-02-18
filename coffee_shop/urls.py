"""
URL configuration for coffee_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("productos/", include("productos.urls")),
    path("usuarios/", include("usuarios.urls")),
    # clase 22, tarea
    path("", TemplateView.as_view(template_name='base.html'), name='base'),
    # clase 23
    path("ordenes/", include("ordenes.urls")),
]

# clase 27 - tarea
from rest_framework.routers import SimpleRouter
from productos.views import ProductoAPI
from ordenes.views import OrdenAPI
router = SimpleRouter()
router.register(r'api/prod', ProductoAPI, basename='producto-api')
router.register(r'api/ord', OrdenAPI, basename='orden-api')
urlpatterns += router.urls

# para imagenes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)