from django.urls import path 
from .views import registrarse, ingresar, inicio, libro
from . import views

urlpatterns = [
   
    path('registrarse',registrarse,name="registrarse"),
    path('ingresar',ingresar,name="ingresar"),
    path('inicio',inicio,name="inicio"),
    path('libro',libro,name="libro"),
    path('<int:id>/editar/', views.editar_libro, name='editar_libro'),
    path('<int:id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
    path('crear', views.crear_libro, name='crear_libro'),
    path('<int:id>/', views.detalle_libro, name='detalle_libro'),
]