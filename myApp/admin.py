from django.contrib import admin
from .models import Categoria, CategoriaUsuario, Libro, Usuario

# Register your models here.

admin.site.register(Categoria)
admin.site.register(CategoriaUsuario)
admin.site.register(Usuario)
admin.site.register(Libro)