from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Agrega aquí más rutas según sea necesario
]