
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import generics, permissions, serializers, viewsets
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse

from activities.serializers import PreguntaSeleccionMultipleSerializer, CalificacionSerializer, RespuestaSeleccionMultipleSerializer, MarcaSerializer
from activities.models import Calificacion, PreguntaOpcionMultiple, RespuestmultipleEstudiante, Opcionmultiple, Marca


class DetailPreguntaSeleccionMultiple(generics.RetrieveUpdateDestroyAPIView, ListModelMixin):
    serializer_class = PreguntaSeleccionMultipleSerializer
    lookup_url_kwarg = "marca"

    def get_queryset(self):
        marca = self.kwargs.get(self.lookup_url_kwarg)
        return PreguntaOpcionMultiple.objects.filter(marca=marca)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)


class PreguntaView(ListModelMixin, CreateModelMixin, GenericAPIView):
    # Add permissions to the view
    # permission_classes = [IsAuthenticated]

    # Add filter fields for the API
    filterset_fields = ("actividad",)
    # clase serializer para la transformacion de datos del request
    serializer_class = PreguntaSeleccionMultipleSerializer

    # def get_queryset(self):
    # actividad = self.request.query_params.get('actividad')
    # return PreguntaOpcionMultiple.objects.filter(actividad=actividad)

    def perform_create(self, serializer):
        # actividad = get_object_or_404(
        #    Actividad, id=self.request.data.get('actividad'))
        return serializer.save()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RespuestaSeleccionMultipleView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = RespuestmultipleEstudiante.objects.all()
    # clase serializer para la transformacion de datos del request
    serializer_class = RespuestaSeleccionMultipleSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
         # Validacion de respuesta en blanco (null)
        if self.request.data['respuestmultiple']:
            opcion = Opcionmultiple.objects.filter(
                id=self.request.data['respuestmultiple'])
            pregunta = opcion[0].preguntaSeleccionMultiple
            # valida si el intento de la respuesta es menor o igual al max de intentos permitidos
            if int(self.request.data['intento']) <= pregunta.numeroDeIntentos:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                msj = {'max_attemps': 'Número de intentos maximos excedido'}
                return Response(msj, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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


class MarcaApi(ListModelMixin, GenericAPIView):
    serializer_class = MarcaSerializer

    def get_queryset(self):
        content = self.request.query_params.get('contenido', None)
        return Marca.objects.filter(contenido=content)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)


def intentos_max(request):
    if request.method == 'GET':
        pregunta = request.GET.get('id_pregunta')        
        estudiante = request.GET.get('id_estudiante')        
        opciones = Opcionmultiple.objects.filter(
            preguntaSeleccionMultiple=pregunta)

        respuestas = RespuestmultipleEstudiante.objects.filter(
            estudiante=estudiante)
        resps = []

        for respuesta in respuestas:
            for opcion in opciones:
                if respuesta.respuestmultiple == opcion:
                    print('ALGO')
                    if respuesta.intento:
                        resps.append(respuesta.intento)
        if len(resps) > 0:
            max_int = max(resps)
        else: max_int = 0

        print(max_int)
        return JsonResponse({'ultimo_intento': max_int}, status=status.HTTP_200_OK)