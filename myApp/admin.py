from django.contrib import admin
from .models import Tipo_usuario,Usuario,Categoria,Libro

# Register your models here.
admin.site.register(Tipo_usuario)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Libro)