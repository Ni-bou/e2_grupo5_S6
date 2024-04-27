from rest_framework import serializers
from myApp.models import Libro, Categoria

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = [ 'codigo_isbn', 'nombre', 'descripcion', 'imagen', 'categoria']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields = ['nombre']