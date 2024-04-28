from django.urls import path 
from .views import registrarse, inicio, libro,ingresar,cerrar_sesion, editar_usuario, vista_api,cambiar_clave
from . import views


urlpatterns = [
   
    path('',inicio,name="inicio"),
    path('registrarse',registrarse,name="registrarse"),
    path('ingresar',ingresar,name="ingresar"),
    path('inicio',inicio,name="inicio"),
    path('libro',libro,name="libro"),
    path('vista_api', vista_api,),

    
    path('<int:id>/editar/', views.editar_libro, name='editar_libro'),
    path('<int:id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
    path('crear', views.crear_libro, name='crear_libro'),
    path('<int:id>/', views.detalle_libro, name='detalle_libro'),
    path('cerrar-sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('libro/<int:id>/', views.detalle_libro, name='detalle_libro'),

    
    path('editar_usuario', editar_usuario, name='editar_usuario'),
    path('recuperar_contrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),
    path('cambiar_clave', cambiar_clave, name='cambiar_clave'),
]