from django.shortcuts import render
from myApp.models import Libro, Categoria
from .serializers import LibroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@csrf_exempt
@api_view(['POST'])
def login (request):
    data = JSONParser().parse(request)

    username = data['username']
    password = data['password']

    try :
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response('Usuario incorrecto')
    
    pass_valido = check_password(password, user.password)

    if not pass_valido: 
        return Response('Contraseña incorrecta')
    
    token, created = Token.objects.get_or_create(user=user)
    return Response(token.key)


#COMENTARIO DE SEGURIDAD PARA SABER SI AL CAMBIAR DE RAMA GIT GUARDA LOS CAMBIOS