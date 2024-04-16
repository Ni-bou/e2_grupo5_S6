from django.db import models

# Create your models here.#los modelos son las tablas que se haran en nuestra base de datos despues de que django se encargue de mandar la creación a la base de datos


#tabla  tipo usuario
class Tipo_usuario(models.Model):
    id_tipo_usuario = models.IntegerField(primary_key=True, verbose_name='Id tipo usuario')
    descripcion = models.CharField(max_length=15, verbose_name='Nombre tipo usuario')

	#Denis: aquí cambiamos la funcion que obteniamos el nombre por el nombre de la funcion que hicimos mas abajo
    def __str__(self):
        return self.get_code_name()

    #Denis: función que obtenga el id de los usuarios en este caso, ISBN es el codigo al inicio
    def get_code_name(self):
        return f" ISBN:{self.id_tipo_usuario} -{self.descripcion}"

# tabla  usuario
class Usuario(models.Model):
	id_usuario = models.AutoField(primary_key = True, verbose_name='Id usuario')
	username = models.CharField(max_length=30, verbose_name='username')
	useremail = models.EmailField(verbose_name='email')
	password = models.CharField(max_length=255, verbose_name='password')
	id_tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE, verbose_name='Tipo_de_usuario')
     
	#esto es para visualizar en la pantalla admin de django
	def __str__(self):
		return self.get_name_code()
    #Denis: función que muestra en la pantalla del administrador django el id tipo usuario y nombre,ISBN es el codigo al inicio 
	def get_name_code(self):
		return f" ISBN:{self.id_usuario} -{self.username}-{self.useremail}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre
    
class Libro(models.Model):
    codigo_isbn = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    imagen = models.ImageField(upload_to='libros/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='libros')