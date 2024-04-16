from django.shortcuts import render
from myApp.models import Usuario


# Create your views here.
def listado_usuarios(request):
        return render(request, 'html/listado_usuarios.html')

#def recuperar_contrasena(request):
    #if request.method == 'POST':
       # usuarios = Usuario.objects.all() #trae todos los usuarios
        #useremail1 = request.POST.get('email')

    #for usuario in usuarios: #hace un for por cada usuario en la tabla usuario
        #if usuario.useremail == useremail1: #este compara si el usuario ya existe
            #mensaje_error = 'El usuario fue encontrado'
            #break

def listado_usuarios(request):
    usuarios = Usuario.objects.all()

    context = {
          'usuarios' : usuarios
    }

    return render(request, 'html/listado_usuarios.html', context)