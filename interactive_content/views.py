# Create your views here.
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.utils import json

from interactive_content.models import Contenido, Curso, ContenidoInteractivo
from interactive_content.serializers import ContenidoSerializer, CursoSerializer


def get_contents(user_id):
    # Verificar que el docente tenga contenido creado
    try:
        # Recuperar el contenido que creó el profesor
        contents_list = Contenido.objects.filter(profesor_id=user_id)
    except (KeyError, Contenido.DoesNotExist):
        # devolver vacio si no existe contenido creado por el usuario
        return JsonResponse({})
    else:
        # Devolver los resultados de la consulta en formato JSON
        serializer_class = ContenidoSerializer(contents_list, many=True)
        response = Response(serializer_class.data, status=status.HTTP_200_OK)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response


def set_contents(resources, user_id):
    # Verificar que el docente sea el propietario del curso
    contenido_id = resources['contenido']
    cursos_ids = resources['cursos']
    get_object_or_404(Contenido, profesor_id=user_id, pk=contenido_id)
    objetos = (ContenidoInteractivo(tiene_retroalimentacion=True,
                                    tiempo_disponibilidad=datetime.now(),
                                    contenido_id=contenido_id,
                                    curso_id=i
                                    ) for i in cursos_ids)
    ContenidoInteractivo.objects.bulk_create(objetos)
    return JsonResponse(resources)


# Verificar que solo sea un usuario profesor el que acceda a este endpoint
# Remove this authentication_classes. Only for testing
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def contents_view(request):
    # Tomando información del usuario
    user_id = request.user.id
    if request.method == 'GET':
        return get_contents(user_id)
    elif request.method == 'POST':
        resources = json.loads(request.body)
        return set_contents(resources, user_id)


# Verificar que solo sea un usuario profesor el que acceda a este endpoint
# Remove this authentication_classes. Only for testing
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def courses_view(request):
    # Tomando información del usuario
    user_id = request.user.id
    # Verificar que el docente tenga contenido creado
    try:
        # Recuperar el contenido que creó el profesor
        contents_list = Curso.objects.filter(profesor_id=user_id)
    except (KeyError, Curso.DoesNotExist):
        # devolver vacio si no existe contenido creado por el usuario
        return JsonResponse({})
    else:
        # Devolver los resultados de la consulta en formato JSON
        serializer_class = CursoSerializer(contents_list, many=True)
        response = Response(serializer_class.data, status=status.HTTP_200_OK)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response
