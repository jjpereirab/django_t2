from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import VistaRegistro

urlpatterns = [
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # clase 23
    path('registro/', VistaRegistro.as_view(), name='registro'),
]