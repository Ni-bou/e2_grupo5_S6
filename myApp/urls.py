from django.urls import path 
from .views import registrarse, ingresar, inicio, libro

urlpatterns = [
   
    path('registrarse',registrarse,name="registrarse"),
    path('ingresar',ingresar,name="ingresar"),
    path('',inicio,name="inicio"),
    path('libro',libro,name="libro"),
   

]