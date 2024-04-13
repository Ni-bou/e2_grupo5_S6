from django.shortcuts import render
from .models import Usuario

# Create your views here.
def registrarse(request):
    return render(request, 'html_apps/registrarse.html')

def ingresar(request):
    return render(request, 'html_apps/ingresar.html')

def inicio(request):
    return render(request, 'html_apps/inicio.html')

def libro(request):
    return render(request, 'html_apps/libro.html')

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
        