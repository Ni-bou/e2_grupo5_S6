from django.shortcuts import get_object_or_404, render, redirect
from .models import Libro, Categoria, CategoriaUsuario, Usuario
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def ingresar(request):
    return render(request, 'registration/login.html')

def inicio(request):
    return render(request, 'html_apps/inicio.html')

def libro(request):
    libros = Libro.objects.all()
    context = {
        'libros' : libros
    }

    return render(request, 'html_apps/libro.html', context)

def registrarse(request):
    return render(request, 'html_apps/registrarse.html')


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
    libro = get_object_or_404(Libro, id=id)

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
    libro = get_object_or_404(Libro, id=id)

    context = {
        'libro': libro
    }

    return render (request, 'html_apps/detalle.html', context)

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.delete()

    messages.success(request, 'Se ha eliminado el libro correctamente')


    return redirect('libro')
       

def crear_usuario(request):
    if request.method == "POST":
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')
        password = request.POST.get('password')

        if Usuario.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('registrarse')
        
        categoria_cliente = CategoriaUsuario.objects.get(id_tipo_usuario=2)

        usuario = Usuario.objects.create(
            username=username,
            useremail=useremail,
            password=password,
            id_tipo_usuario=categoria_cliente
        )

        messages.success(request, 'Se ha creado el usuario correctamente')

        return redirect('registrarse')

    return render(request, 'html_apps/registrarse.html')

def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('libro')
        else:
            context = {
                'error' : 'Error intente nuevamente'
            }
        
            return render(request, 'registration/login.html', context)
    
    return render (request, '')

def logout_view(request):
    logout(request)
    return redirect('login')