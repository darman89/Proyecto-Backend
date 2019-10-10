# Create your views here.
from datetime import datetime

from django.db.models import Subquery
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from interactive_content.models import Contenido, Curso, ContenidoInteractivo
from interactive_content.serializers import CursoSerializer, ContenidoInteractivoSerializer


def get_contents(user_id):
    # Verificar que el docente tenga contenido creado
    try:
        # Recuperar el contenido que creó el profesor
        contents_list = ContenidoInteractivo.objects.filter(contenido__profesor_id=user_id).select_related('contenido')
    except (KeyError, ContenidoInteractivo.DoesNotExist):
        # devolver vacio si no existe contenido creado por el usuario
        return JsonResponse({})
    else:
        # Devolver los resultados de la consulta en formato JSON
        serializer_class = ContenidoInteractivoSerializer(contents_list, many=True)
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
@authentication_classes([TokenAuthentication])
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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def courses_view(request, content_id):
    # Tomando información del usuario
    user_id = request.user.id
    # Verificar que el docente tenga contenido creado
    try:
        # Recuperar el contenido que creó el profesor
        contents = ContenidoInteractivo.curso.through.objects.filter(contenidointeractivo_id=content_id)
        if not contents:
            contents_list = Curso.objects.filter(profesor_id=user_id)
        else:
            contents_list = Curso.objects.filter(profesor_id=user_id).exclude(pk=Subquery(contents.values('curso_id')))

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


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class ContentCreator(APIView):
    def post(self, request, *args, **kwargs):
        new_content_data = request.data
        courses = new_content_data.pop('cursos_seleccionados',None)
        contenido = Contenido.objects.Create(profesor=request.user, **new_content_data)
        if courses:
            interactive_content = ContenidoInteractivo.objects.create(contenido=contenido,
                                                                      tiene_retroalimentacion=False)
            for selected_course in courses:
                course_obj = Curso.objects.get(pk=selected_course['id'], profesor=request.user)
                interactive_content.curso.add(course_obj)
        return Response(status=status.HTTP_201_CREATED)
