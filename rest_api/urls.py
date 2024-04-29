from django.urls import path
from .import views 
from .views import lista_libros,lista_categoria

#Api/

urlpatterns = [
    path ('lista_libros/' , lista_libros, name='lista_libros'),
    path ('libros/<id>/', views.vista_libro, name='vista_libro'),
    path ('lista_categoria/' , lista_categoria, name='lista_categoria'),
    ] #se crea la url de la api para que se pueda acceder a la lista de libros