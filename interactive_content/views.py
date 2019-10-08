from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from django.shortcuts import get_object_or_404

from interactive_content.serializers import ContInteractivoSerializer
from interactive_content.models import ContenidoInteractivo, Contenido, Curso

# Create your views here.

class ContInteractivoView(ListModelMixin, CreateModelMixin, GenericAPIView):
    # queryset usado para retornar los objetos requeridos
    queryset = ContenidoInteractivo.objects.all()
    # clase serializer para la transformacion de datos del request
    serializer_class = ContInteractivoSerializer

    def perform_create(self, serializer):
        contenido = get_object_or_404(
            Contenido, id=self.request.data.get('contenido'))
        return serializer.save(contenido=contenido)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
