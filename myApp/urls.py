from django.urls import path 
from .views import registrarse, inicio, libro,ingresar

urlpatterns = [
   
    path('registrarse',registrarse,name="registrarse"),
    path('ingresar',ingresar,name="ingresar"),
    path('',inicio,name="inicio"),
    path('libro',libro,name="libro"),

   

]