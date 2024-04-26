from django.urls import path 
from .views import registrarse, ingresar, inicio, libro, logout_view
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   
    path('registrarse', views.crear_usuario,name="registrarse"),
    path('login',views.inicio_sesion,name="inicio_sesion"),
    path('inicio',inicio,name="inicio"),
    path('libro',libro,name="libro"),
    path('<int:id>/editar/', views.editar_libro, name='editar_libro'),
    path('<int:id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
    path('crear', views.crear_libro, name='crear_libro'),
    path('logout', logout_view, name='logout'),
    path('<int:id>/', views.detalle_libro, name='detalle_libro'),
]