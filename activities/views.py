
from rest_framework.generics import GenericAPIView,ListCreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import generics, permissions, serializers, viewsets
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from activities.serializers import PreguntaSeleccionMultipleSerializer, CalificacionSerializer
from activities.models import Calificacion, PreguntaOpcionMultiple

class DetailPreguntaSeleccionMultiple(generics.RetrieveUpdateDestroyAPIView):
    queryset = PreguntaOpcionMultiple.objects.all()
    serializer_class = PreguntaSeleccionMultipleSerializer

class PreguntaView(ListModelMixin, CreateModelMixin, GenericAPIView):
     # Add permissions to the view
     # permission_classes = [IsAuthenticated]

     # Add filter fields for the API
     filterset_fields = ("actividad",)
     # clase serializer para la transformacion de datos del request
     serializer_class = PreguntaSeleccionMultipleSerializer

     #def get_queryset(self):
         #actividad = self.request.query_params.get('actividad')
         #return PreguntaOpcionMultiple.objects.filter(actividad=actividad)

     def perform_create(self, serializer):
         #actividad = get_object_or_404(
         #    Actividad, id=self.request.data.get('actividad'))
         return serializer.save()

     def get(self, request, *args, **kwargs):
         return self.list(request, *args, *kwargs)

     def post(self, request, *args, **kwargs):
         return self.create(request, *args, **kwargs)
      

class CalificarAPI(ListCreateAPIView):
    # Add filter fields for the API
    filterset_fields = ("estudiante", "actividad")
    # serializer usado para la transformacion de datos
    serializer_class = CalificacionSerializer

    # queryset para retornar las calificaciones de un estudiante
    def get_queryset(self):
        student = self.request.query_params.get('estudiante', None)
        activity = self.request.query_params.get('actividad', None)
        if (student):
            return Calificacion.objects.filter(estudiante=student)
        if (activity):
            return Calificacion.objects.filter(actividad=activity)

