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
    id_tipo_usuario = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.id_tipo_usuario)


class Usuario(models.Model):
    password = models.CharField(max_length=100)
    useremail = models.EmailField(max_length=200)
    username = models.CharField(max_length=200)
    id_tipo_usuario = models.ForeignKey(CategoriaUsuario, on_delete=models.CASCADE, related_name='usuario')

    def __str__(self):
        return f"{self.username} - {self.id_tipo_usuario}"