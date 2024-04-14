from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    codigo_isbn = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    imagen = models.ImageField(upload_to='libros/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='libros')

    def __str__(self):
        return self.nombre

class CategoriaUsuario(models.Model):
    tipoUsuario = models.CharField(max_length=20)

    def __str__(self):
        return self.tipoUsuario


class Usuario(models.Model):
    usuario = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    nombreApellido = models.CharField(max_length=200)
    tipoUsuario = models.ForeignKey(CategoriaUsuario, on_delete=models.CASCADE, related_name='usuario')

    