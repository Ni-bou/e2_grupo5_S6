from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Libro, Categoria, Tipo_usuario, Usuario
from django.contrib import messages
from pathlib import Path
from django.contrib import sessions
from django.contrib.auth import logout
import requests



# Para meterse a cada pagina
def registrarse(request):
    return render(request, 'html_apps/registrarse.html')

def ingresar(request):
    return render(request, 'html_apps/ingresar.html')

def inicio(request):
    return render(request, 'html_apps/inicio.html')

import requests
from django.shortcuts import render

def vista_api(request):
    # URL de la API
    url = "https://harry-potter-api.onrender.com/personajes"
    if  request.method == 'GET':
        if  request.session.get('usuario'):
            response = requests.get(url)

            if response.status_code == 200:
                personajes = response.json()
            else:
                personajes = []
            context = {
                'personajes': personajes
            }
            return render(request, 'html_apps/vista_api.html', context)
        else:
                            return redirect('ingresar')
    else:
            return redirect('inicio')


import requests
from django.shortcuts import render

def vista_api_libros(request):
    # URL de la API
    url = "https://gutendex.com/books/"
    if  request.method == 'GET':
        if  request.session.get('usuario'):
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                books = data.get('results', [])
                # Iterar sobre los libros para agregar la URL de la imagen directamente al diccionario
                for book in books:
                    book['image_url'] = book['formats'].get('image/jpeg', '')
            else:
                books = []

            context = {
                'books': books
            }

            return render(request, 'html_apps/vista_api_libros.html', context)
        else:
                    return redirect('ingresar')
    else:
            return redirect('inicio')

def inicio(request):
    if request.method == 'GET':
        if  request.session.get('usuario'):
            usuario = request.session.get('usuario')
            if usuario:
                print("mandando un usuario")
                return render(request, 'html_apps/inicio.html', {'usuario': usuario})
            else:
                return redirect('ingresar')
        else:
            return redirect('ingresar')
    else:
            return redirect('inicio')
    
def editar_usuario(request):
    if request.method == 'POST':
        mensaje_confirmacion = None
        usuario_actualizar = request.session.get('usuario')
        print(usuario_actualizar)
        if usuario_actualizar:
            usuario = Usuario.objects.get(id_usuario=usuario_actualizar['id_usuario'])
            print(usuario)
            useremail1 = request.POST.get('nombre')
            email1 = request.POST.get('email')

            usuario.username = useremail1
            usuario.useremail = email1
            usuario.save()
            if usuario:
                print("Datos de usuario actualizados:", usuario)
                mensaje_confirmacion= 'Datos de usuario actualizados'
                request.session['usuario'] = {'id_usuario': usuario.id_usuario,'username': usuario.username,'email':usuario.useremail}
            return render(request, 'html_apps/editar_usuario.html', {'usuario': usuario, 'mensaje_confirmacion':mensaje_confirmacion})
        return  redirect('editar_usuario')
    return  redirect('editar_usuario')
    
def cambiar_clave(request):
    print("entro a cambiar la clave 2222")
    mensaje_clave = None
    error_contrasena=None
    usuario_contras = request.session.get('usuario_id')
    print("viendo al usuarioi",usuario_contras)
    usuario = Usuario.objects.filter(id_usuario=usuario_contras).first()

    if request.method == 'POST':
        print("usuario")
        print(usuario_contras)
        if usuario_contras:
            usuario = Usuario.objects.filter(id_usuario=usuario_contras).first()
            print(usuario)
            clave = request.POST.get('pass')
            clave1 = request.POST.get('newpass')
            
            if len(clave) < 6 or len(clave) >= 18:
                error_contrasena = 'La contraseña debe tener entre 6 y 18 caracteres'
            elif not (any(c.isupper() for c in clave) and any(c.isdigit() for c in clave)):
                error_contrasena = 'La contraseña debe contener al menos una letra mayúscula, un número y un caracter'
            else:
                print("cumple con la contraseña222")
        
                if clave == clave1:#que las claves sean iguales
                    print("la clave es la misma")
                    usuario.password = clave
                    usuario.save()
                    mensaje_clave = 'Contraseña cambiada'
                    return  redirect('inicio')
                else:
                    print("la contraseña no es la misma")
                    error_contrasena= 'la clave no es la misma'
        else: 
            print("debe rellenar los dos espacios ")
            error_contrasena= 'debe rellenar los dos espacios '
            

    return render(request, 'html_apps/cambiar_clave.html', {'mensaje_error': error_contrasena,'mensaje_clave':mensaje_clave})
                   

#para obtener el usuario en el login
def ingresar(request):
    mensaje_error = None
    mensaje_Bienvenida = None
    if request.method == 'POST':
        useremail = request.POST.get('user')
        password = request.POST.get('pass')
        print("metodo post activo")
        if not password :
            print("entro para redirigir")
            mensaje_error = 'es para probar'
            return render(request, 'html_apps/recuperar_contrasena.html')

        else:
            useremail = request.POST.get('user')
            password = request.POST.get('pass')
            print("Datos del form", useremail, password)

            usuarioBD = Usuario.objects.filter(useremail=useremail).first()
            print(usuarioBD)
            if usuarioBD is not None:
                if usuarioBD.password == password:
                    id_tipo_usuario = usuarioBD.id_tipo_usuario.id_tipo_usuario
                    print("trae al usuario de la base de datos")
                    try:
                        usuarioBD = Usuario.objects.filter(useremail=useremail).first()
                        request.session['usuario'] = {'id_usuario': usuarioBD.id_usuario,'username': usuarioBD.username,'email':useremail, 'password':usuarioBD.password,'mascota_name':usuarioBD.mascota_name,'id_tipo_usuario':id_tipo_usuario}
                        return redirect('inicio')
                    except Tipo_usuario.DoesNotExist:
                        print("problema de la pagina")
                        mensaje_error = 'problemas de la pagina'
                        return render(request, 'html_apps/ingresar.html')

                else:
                    print("La contraseña no es la misma")
                    mensaje_error = 'La contraseña no es la misma'
            else:
                print("El usuario no existe")
                mensaje_error = 'El usuario no existe'
            
    return render(request, 'html_apps/ingresar.html', {'mensaje_error': mensaje_error,'mensaje_bienvenida':mensaje_Bienvenida})
    
def recuperar_contrasena(request):
    print("entro a la funcion recuperar_contrasena")
    mensaje_error: None
    useremail = request.POST.get('correo')
    mascota_name = request.POST.get('mascotaname')
    if request.method == 'POST':
        print("entro al POSTmetodo")
        usuarioBD = Usuario.objects.filter(useremail=useremail).first()
        
        if usuarioBD is not None:
            print("para ver al usuario",usuarioBD)
            if usuarioBD.mascota_name == mascota_name:
                print("se envio el usuario a la pagina cambiar_clave")
                request.session['usuario_id'] = usuarioBD.id_usuario
                return redirect('cambiar_clave')

        else:
                print("La contraseña no es la misma")
                mensaje_error = 'La contraseña no es la misma o ese usuario no existe'
                
    return render(request, 'html_apps/recuperar_contrasena.html')

def registrarse(request):
    mensaje_error = None #para utilizarlo como mensaje en un label de bajo del boton
    error_contrasena = None #para el error de contraseña
    usuario_registrado = None#mensaje de registrar efectivo
    
    if request.method == 'POST': #si el metodo de llama es post
        #obtenemos lso datos de los input segun el id que tienen
        username1 = request.POST.get('name')
        password = request.POST.get('first_pass')
        password2 = request.POST.get('second_pass')
        useremail1 = request.POST.get('email')
        mascota1 = request.POST.get('mascot')
        
        print("Datos del form:", username1, useremail1, password, password2,mascota1)#para ver los datos por consola
        if useremail1 and password and password2 and mascota1:  # que tengan todos los datos
            print("cumple todos los inputs")

            if len(password) < 6 or len(password) >= 18:
                error_contrasena = 'La contraseña debe tener entre 6 y 18 caracteres'
            elif not (any(c.isupper() for c in password) and any(c.isdigit() for c in password)):
                error_contrasena = 'La contraseña debe contener al menos una letra mayúscula, un número y un caracter'

            else:
                print("cumple con la contraseñá")
        
                if password == password2:#que las claves sean iguales
                    print("la clave es la misma")
                    # Obtener el último usuario creado en la tabla Usuario
                    try:
                        ultimo_usuario = Usuario.objects.latest('id_usuario')
                        nuevo_id_usuario = ultimo_usuario.id_usuario + 1
                    except Usuario.DoesNotExist:
                        nuevo_id_usuario = 1
                    
                    usuarios = Usuario.objects.all() #trae todos los usuarios
                    for usuario in usuarios: #hace un for por cada usuario en la tabla usuario
                        if usuario.useremail == useremail1: #este compara si el usuario ya existe
                            mensaje_error = 'El usuario ya existe'
                            break
                    
                    if not mensaje_error:  # Si no hay error
                        try:
                            tipo_usuario_default = Tipo_usuario.objects.get(pk=2)
                            nuevo_usuario = Usuario.objects.create(id_usuario=nuevo_id_usuario, username=username1, useremail=useremail1, password=password, mascota_name=mascota1, id_tipo_usuario=tipo_usuario_default)
                            print("Nuevo usuario creado:", nuevo_usuario)
                            usuario_registrado = "¡Usuario registrado exitosamente!"
                            if usuario in usuarios:
                                try:
                                    usuarioBD = Usuario.objects.filter(useremail=useremail1).first()
                                    id_tipo_usuario = usuarioBD.id_tipo_usuario.id_tipo_usuario
                                    request.session['usuario'] = {'username': usuarioBD.username, 'tipo': id_tipo_usuario}
                                    return render(request, 'html_apps/registrarse.html', {'mensaje_error': mensaje_error, 'error_contrasena': error_contrasena,'usuario_registrado':usuario_registrado})
                                except Tipo_usuario.DoesNotExist:
                                    print("no fue guardado correctamente")
                                    
                        except Tipo_usuario.DoesNotExist:
                            print("El Tipo_usuario con pk=2 no existe.")
                else:
                    print("la contraseña no es la misma")
                    mensaje_error = 'Las contraseñas no coinciden'
        else:
            print("hubo un error en el formulario")
            mensaje_error = 'Hubo un error en el formulario. Por favor, complete todos los campos.'
        

    return render(request, 'html_apps/registrarse.html', {'mensaje_error': mensaje_error, 'error_contrasena': error_contrasena,'usuario_registrado':usuario_registrado})

def libro(request):
    if request.method == 'GET':
        if request.session.get('usuario'):
            libros = Libro.objects.all()
            context = {
                'libros': libros
            }
            return render(request, 'html_apps/libro.html', context)
        else:
            return redirect('ingresar')
    else:
        return redirect('inicio')
    
def crear_libro(request):
    if request.method == "POST":
        categoria_id = request.POST.get('categoria')
        categoria = get_object_or_404(Categoria, id=categoria_id)

        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')

        Libro.objects.create(
            codigo_isbn=codigo,
            nombre=nombre,
            descripcion=descripcion,
            imagen=imagen,
            categoria=categoria
        )
        messages.success(request, 'Se ha creado el libro correctamente')

        return redirect('libro')


    categorias = Categoria.objects.all()

    context = {
        'categorias': categorias
    }
    return render(request, 'html_apps/crear.html', context)

def editar_libro(request, id):
    libro = get_object_or_404(Libro, codigo_isbn=id)

    if request.method == "POST":
        categoria_id = request.POST['categoria']
        categoria = get_object_or_404(Categoria, id=categoria_id)

        libro.nombre = request.POST['nombre']
        libro.codigo_isbn = request.POST['codigo']
        libro.descripcion = request.POST.get('descripcion', '')
        libro.categoria = categoria

        if 'imagen' in  request.FILES:
            libro.imagen = request.FILES['imagen']

        libro.save()
        messages.success(request, 'Se ha editado el libro correctamente')
        return redirect('libro')

    categorias = Categoria.objects.all()
    context = {
        'libro': libro,
        'categorias':categorias
    }

    return render(request, 'html_apps/editar.html', context)


def detalle_libro(request, id):
    libro = get_object_or_404(Libro, codigo_isbn=id)
    print("ID del libro:", libro.codigo_isbn)  # Añade esta línea para verificar el valor del ID

    context = {
        'libro': libro
    }

    return render (request, 'html_apps/detalle.html', context)

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, codigo_isbn=id)
    libro.delete()

    messages.success(request, 'Se ha eliminado el libro correctamente')


    return redirect('libro')

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')