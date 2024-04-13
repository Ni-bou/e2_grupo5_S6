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
                print("Datos del form",useremail,password)

                usuarioBD = Usuario.objects.filter(useremail=useremail).first()
                print(usuarioBD)
                if usuarioBD is not None:
                        if usuarioBD.password == password:
                                if usuarioBD.perfil == 1:
                                        print("administrador")
                                        return render(request,'html_apps/ingresar.html')
                                if usuarioBD.perfil == 2:
                                        print("usuario normal")
                                        return render(request,'html_apps/ingresar.html')
                                else:
                                        print("No se encontro perfil")
                                        return render(request,'html_apps/ingresar.html')
                        else:
                                print("Password Incorrecta")
                                return render(request,'html_apps/ingresar.html')
                else:
                        print("Usuario no existe")
                        return render(request,'html_apps/ingresar.html')
        else:
                return render(request,'html_apps/ingresar.html')
        

        