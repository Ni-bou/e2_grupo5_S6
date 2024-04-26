from django.urls import path
from .import views 
from .views import lista_libros

#Api/

urlpatterns = [
    path ('lista_libros/' , lista_libros, name='lista_libros'),
    path ('libros/<id>/', views.vista_libro, name='vista_libro'),
    ] #se crea la url de la api para que se pueda acceder a la lista de libros