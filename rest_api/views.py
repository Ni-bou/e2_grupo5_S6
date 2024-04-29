from django.shortcuts import render
from myApp.models import Libro,Categoria
from .serializers import LibroSerializer
from .serializers import CategoriaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated,])
def lista_libros(request):
    if request.method == 'GET':
        libro = Libro.objects.all()
        serializer = LibroSerializer(libro, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LibroSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
@api_view(['GET', 'PUT','PATCH' 'DELETE'])
@permission_classes([IsAuthenticated,])
def vista_libro(request, id):
    try:
        libro = Libro.objects.get(id=id)
    except Libro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LibroSerializer(libro)
        return Response(serializer.data)
    
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = LibroSerializer(libro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#COMENTARIO DE SEGURIDAD PARA SABER SI AL CAMBIAR DE RAMA GIT GUARDA LOS CAMBIOS
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated,])
def lista_categoria(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
@api_view(['GET', 'PUT','PATCH' 'DELETE'])
@permission_classes([IsAuthenticated,])
def vista_categoria(request, id):
    try:
        categoria = Categoria.objects.get(nombre=id)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
