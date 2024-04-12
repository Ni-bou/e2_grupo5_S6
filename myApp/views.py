from django.shortcuts import render

# Create your views here.
def registrarse(request):
    return render(request, 'html_apps/registrarse.html')

def ingresar(request):
    return render(request, 'html_apps/ingresar.html')

def inicio(request):
    return render(request, 'html_apps/inicio.html')

def libro(request):
    return render(request, 'html_apps/libro.html')