from django.shortcuts import render, redirect
from .models import Usuario
from .forms import Registro_form
from django.contrib.auth.models import User

# Para meterse a cada pagina
def registrarse(request):
    return render(request, 'html_apps/registrarse.html')

def ingresar(request):
    return render(request, 'html_apps/ingresar.html')

def inicio(request):
    return render(request, 'html_apps/inicio.html')

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


#para registrarse
def registrarse(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('firstpass')
        password2 = request.POST.get('secondpass')
        useremail = request.POST.get('email')
        
        print("Datos del form",username, useremail, password,password2)
        form = Registro_form(request.POST)
        # Verificar que las contraseñas coincidan
        if password == password2:
            if form.is_valid():
                id_tipo_usu = 2
                # Crear un nuevo usuario en la base de datos
                nuevo_usuario = form.save()
                print("se guardaron los datos")

                username = form.cleaned_data['username']
                useremail = form.cleaned_data['useremail']
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']
                id_tipo_usuario = form.cleaned_data['id_tipo_usu']
                print("entro para limpiar")
                
            else:
                print("la contraseña no es la misma")
                # Redirigir a la página de inicio u otra página de tu elección
                return redirect('html_apps/ingresar.html')
        return 
    else:
        form = Registro_form()
        print("vuelva a ingresar")

    return render(request, 'html_apps/registrarse.html')