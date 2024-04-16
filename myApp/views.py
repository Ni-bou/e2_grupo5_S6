from django.shortcuts import render, redirect
from .models import Usuario, Tipo_usuario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Para meterse a cada pagina
def registrarse(request):
    return render(request, 'html_apps/registrarse.html')

def ingresar(request):
    return render(request, 'html_apps/ingresar.html')

def inicio(request):
    return render(request, 'html_apps/inicio.html')

@login_required
def libro(request):
    return render(request, 'html_apps/libro.html')



#para obtener el usuario en el login
def ingresar(request):
    if request.method == 'POST':
        useremail = request.POST.get('user')
        password = request.POST.get('pass')
        print("Datos del form", useremail, password)

        usuarioBD = Usuario.objects.filter(useremail=useremail).first()
        print(usuarioBD)
        if usuarioBD is not None:
            if usuarioBD.password == password:
                id_tipo_usuario = usuarioBD.id_tipo_usuario.id_tipo_usuairo
                if id_tipo_usuario == 1:
                    print("administrador")
                    return render(request, 'html_apps/ingresar.html')
                elif id_tipo_usuario == 2:
                    print("usuario normal")
                    return render(request, 'html_apps/ingresar.html')
                else:
                    print("No se encontró perfil")
                    return render(request, 'html_apps/ingresar.html')
            else:
                print("Password Incorrecta")
                return render(request, 'html_apps/ingresar.html')
        else:
            print("Usuario no existe")
            return render(request, 'html_apps/ingresar.html')
    else:
        return render(request, 'html_apps/ingresar.html')


def registrarse(request):
    mensaje_error = None #para utilizarlo como mensaje en un label de bajo del boton
    error_contrasena = None #para el error de contraseña
    usuario_registrado = None#mensaje de registrar efectivo
    
    if request.method == 'POST': #si el metodo de llama es post
        #obtenemos lso datos de los input
        username1 = request.POST.get('name')
        password = request.POST.get('first_pass')
        password2 = request.POST.get('second_pass')
        useremail1 = request.POST.get('email')
        
        print("Datos del form:", username1, useremail1, password, password2)#para ver los datos por consola
        if useremail1 and password and password2:  # que tengan datos
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
                    ultimo_usuario = Usuario.objects.latest('id_usuario')#latest obtiene el ultimo id de los usuarios
                    nuevo_id_usuario = ultimo_usuario.id_usuario + 1 if ultimo_usuario else 1 #crea un usuario, que le suma un digito al id_usuario del ultimo encontrado y si no hay este crea el numero 1
                    
                    usuarios = Usuario.objects.all() #trae todos los usuarios
                    for usuario in usuarios: #hace un for por cada usuario en la tabla usuario
                        if usuario.useremail == useremail1: #este compara si el usuario ya existe
                            mensaje_error = 'El usuario ya existe'
                            break
                    
                    if not mensaje_error:#si no arroja el mensaje anterior entonces agregara al nuevo usuario
                        tipo_usuario_default = Tipo_usuario.objects.get(pk=2)  # Suponiendo que tienes un tipo de usuario por defecto
                        nuevo_usuario = Usuario.objects.create(id_usuario=nuevo_id_usuario, username=username1, useremail=useremail1, password=password, id_tipo_usuario=tipo_usuario_default)
                        print("Nuevo usuario creado:", nuevo_usuario)
                        usuario_registrado ="¡Usuario registrado exitosamente!"
                else:
                    print("la contraseña no es la misma")
                    mensaje_error = 'Las contraseñas no coinciden'
        else:
            print("hubo un error en el formulario")
            mensaje_error = 'Hubo un error en el formulario. Por favor, complete todos los campos.'
        

    return render(request, 'html_apps/registrarse.html', {'mensaje_error': mensaje_error, 'error_contrasena': error_contrasena,'usuario_registrado':usuario_registrado})


