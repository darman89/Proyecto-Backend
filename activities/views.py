from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from django.shortcuts import get_object_or_404

from activities.serializers import MarcaSerializer, ActividadSerializer, RespuestaMultipleEstudianteSerializer
from activities.models import Marca, Actividad, RespuestmultipleEstudiante, Pregunta
from interactive_content.models import ContenidoInteractivo

# Create your views here.


class MarcaView(ListModelMixin, CreateModelMixin, GenericAPIView):
    # queryset usado para retornar los objetos requeridos
    def get_queryset(self):
        # Add filter to get all the activities of a desired Marca
        contenido = self.request.query_params.get('contenido', None)
        return Marca.objects.filter(contenido=contenido)

    # clase serializer para la transformacion de datos del request
    serializer_class = MarcaSerializer

    def perform_create(self, serializer):
        contenido = get_object_or_404(
            ContenidoInteractivo, id=self.request.data.get('contenido'))
        return serializer.save(contenido=contenido)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ActividadView(ListModelMixin, CreateModelMixin, GenericAPIView):
    # queryset usado para retornar los objetos requeridos
    def get_queryset(self):
        # Add filter to get all the activities of a desired Marca
        marca = self.request.query_params.get('marca', None)
        return Actividad.objects.filter(marca=marca)

    # clase serializer para la transformacion de datos del request
    serializer_class = ActividadSerializer

    def perform_create(self, serializer):
        marca = get_object_or_404(
            Marca, id=self.request.data.get('marca'))
        return serializer.save(marca=marca)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RespEstudianteMultipleView(ListModelMixin, CreateModelMixin, GenericAPIView):
    # Add filter fields for the API
    filterset_fields = ("estudiante", "preguntaSeleccionMultiple")

    # queryset usado para retornar los objetos requeridos
    def get_queryset(self):
        # Add filter to get all the answers of a desired student
        estudiante = self.request.query_params.get('estudiante', None)
        return RespuestmultipleEstudiante.objects.filter(estudiante=estudiante)

    # clase serializer para la transformacion de datos del request
    serializer_class = RespuestaMultipleEstudianteSerializer

    def perform_create(self, serializer):
        pregunta = get_object_or_404(
            Pregunta, id=self.request.data.get('preguntaSeleccionMultiple'))
        return serializer.save(preguntaSeleccionMultiple=pregunta)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class RespOpMultEstudiantetFilter(filters.FilterSet):
#     class Meta:
#         model = RespuestmultipleEstudiante
#         fields = ('estudiante', 'preguntaSeleccionMultiple')