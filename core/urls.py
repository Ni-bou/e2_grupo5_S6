from django.urls import path
from .views import listado_usuarios

urlpatterns = [
    path('listado_usuarios', listado_usuarios, name='listado_usuarios'),

    # Agrega aquí más rutas según sea necesario
]