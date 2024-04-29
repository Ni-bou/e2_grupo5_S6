from django.db import models
from pathlib import Path

# Create your models here.#los modelos son las tablas que se haran en nuestra base de datos despues de que django se encargue de mandar la creación a la base de datos


#tabla  tipo usuario
class Tipo_usuario(models.Model):
    id_tipo_usuario = models.IntegerField(primary_key=True, verbose_name='Id tipo usuario')
    descripcion = models.CharField(max_length=30, verbose_name='Nombre tipo usuario')

    def __str__(self):
        return f"ISBN:{self.id_tipo_usuario} - {self.descripcion}"

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, verbose_name='Id usuario')
    username = models.CharField(max_length=30, verbose_name='username')
    useremail = models.EmailField(verbose_name='email')
    password = models.CharField(max_length=255, verbose_name='password')
    mascota_name = models.CharField(max_length=255, verbose_name='mascota_name')
    id_tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE, verbose_name='Tipo usuario')

    def __str__(self):
        return f"ISBN:{self.id_usuario} - {self.username} - {self.useremail}"
    #Denis: función que muestra en la pantalla del administrador django el id tipo usuario y nombre,ISBN es el codigo al inicio 
    def get_name_code(self):
        return f" ISBN:{self.id_usuario} -{self.username}-{self.useremail}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre
    
class Libro(models.Model):
    codigo_isbn = models.AutoField(primary_key=True, verbose_name='codigo_isbn_libro', unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    imagen = models.ImageField(upload_to='libros/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='libros')
    

class Autor_registro_libro(models.Model):
    id_modificación= models.AutoField(primary_key=True, verbose_name='Id_modificación')
    descripcion_realizado = models.CharField(max_length=255, null=True, blank=True)
    codigo_isbn = models.ForeignKey(Libro, on_delete=models.CASCADE, verbose_name='Libro')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='modificación_libro_usuario')

class cantidad_libros(models.Model):
    id_cantidad = models.AutoField(primary_key=True, verbose_name='Id cantidad libros')
    nombre_libro = models.CharField(max_length=30, verbose_name='nombre_libro')
    cantidad = models.IntegerField(max_length=255, null=True, blank=True)
