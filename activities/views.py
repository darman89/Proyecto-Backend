from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import generics, permissions, serializers, viewsets
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from activities.serializers import PreguntaSeleccionMultipleSerializer, RespuestaSeleccionMultipleSerializer

#     PreguntaSerializer, RespuestaMultipleSerializer
# from interactive_content.models import ContenidoInteractivo
# from users.models import Profesor
# from django.http import HttpResponseNotFound
# 
# 
from .models import PreguntaOpcionMultiple
# # Create your views here.
# @csrf_exempt
# def reports(request):
# 
#     #Get correct professor through token or session
#     try:
#         get_the_professor = Profesor.objects.get(id=request.user.id)
#     except:
#         return HttpResponseNotFound()
# 
#     big_json = {}
#     big_json['username'] = get_the_professor.username
#     big_json['first_name'] = get_the_professor.first_name
#     big_json['last_name'] = get_the_professor.last_name
#     big_json['email'] = get_the_professor.email
#     big_json['direccion'] = get_the_professor.direccion
#     big_json['telefono'] = get_the_professor.telefono
#     big_json['facultad'] = get_the_professor.facultad
#     big_json['marcas'] = []
# 
#     marcas = Marca.objects.filter(contenido__contenido__profesor=get_the_professor)
#     for marca in marcas:
# 
#         big_json['marcas'].append({'nombre':marca.nombre,'actividades':[]})
#         actividades = Actividad.objects.filter(marca=marca)
# 
#         for actividad in actividades:
# 
#             big_json['marcas'][-1]['actividades'].append({'nombre':actividad.nombre, 'preguntas':[]})
#             preguntas = Pregunta.objects.filter(actividad=actividad)
# 
#             for pregunta in preguntas:
# 
#                 big_json['marcas'][-1]['actividades'][-1]['preguntas'].append({'pregunta':pregunta.Pregunta, 'tipo':'', 'opciones':[]})
#                 opciones = Respuestmultiple.objects.filter(preguntaSeleccionMultiple=pregunta)
# 
#                 if opciones.count() != 0:
#                     big_json['marcas'][-1]['actividades'][-1]['preguntas'][-1]['tipo'] = 'multiple'
#                     for opcion in opciones:
#                         votos = RespuestmultipleEstudiante.objects.filter(respuestmultiple=opcion).count()
#                         big_json['marcas'][-1]['actividades'][-1]['preguntas'][-1]['opciones'].append({'respuesta':opcion.respuesta, 'esCorrecta': opcion.esCorrecta, 'votos':votos})
#                 else:
#                     big_json['marcas'][-1]['actividades'][-1]['preguntas'][-1]['tipo'] = 'verdadero/falso'
#                     VF = RespuestaVoF.objects.filter(preguntaVoF=pregunta)
#                     for vf in VF:
#                         isCorrect = vf.esCorrecta
#                         howManyTrue = RespuestaEstudianteVoF.objects.filter(preguntaVoF=vf, respuesta=True).count() #"howTrue":value
#                         howManyFalse = RespuestaEstudianteVoF.objects.filter(preguntaVoF=vf, respuesta=False).count() #"howFalse":value
#                         big_json['marcas'][-1]['actividades'][-1]['preguntas'][-1]['opciones'].append(
#                             {'respuesta': vf.esCorrecta, 'numeroVerdadero': howManyTrue, 'numeroFalso': howManyFalse})
# 
#     return JsonResponse(big_json)
# 
# 
# class MarcaView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     # Add permissions to the view
#     # permission_classes = [IsAuthenticated]
# 
#     # queryset usado para retornar los objetos requeridos
#     def get_queryset(self):
#         # Add filter to get all the activities of a desired Marca
#         contenido = self.request.query_params.get('contenido', None)
#         return Marca.objects.filter(contenido=contenido)
# 
#     # clase serializer para la transformacion de datos del request
#     serializer_class = MarcaSerializer
# 
#     def perform_create(self, serializer):
#         contenido = get_object_or_404(
#             ContenidoInteractivo, id=self.request.data.get('contenido'))
#         return serializer.save(contenido=contenido)
# 
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, *kwargs)
# 
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
# 
# 
# class ActividadView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     # Add permissions to the view
#     # permission_classes = [IsAuthenticated]
# 
#     # queryset usado para retornar los objetos requeridos
#     def get_queryset(self):
#         # Add filter to get all the activities of a desired Marca
#         marca = self.request.query_params.get('marca', None)
#         return Actividad.objects.filter(marca=marca)
# 
#     # clase serializer para la transformacion de datos del request
#     serializer_class = ActividadSerializer
# 
#     def perform_create(self, serializer):
#         marca = get_object_or_404(
#             Marca, id=self.request.data.get('marca'))
#         return serializer.save(marca=marca)
# 
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, *kwargs)
# 
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
# 
# 
# class RespEstudianteMultipleView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     # Add permissions to the view
#     # permission_classes = [IsAuthenticated]
# 
#     # Add filter fields for the API
#     filterset_fields = ("estudiante", "respuestmultiple")
# 
#     # queryset usado para retornar los objetos requeridos
#     def get_queryset(self):
#         # Add filter to get all the answers of a desired student
#         estudiante = self.request.query_params.get('estudiante', None)
#         return RespuestmultipleEstudiante.objects.filter(estudiante=estudiante)
# 
#     # clase serializer para la transformacion de datos del request
#     serializer_class = RespuestaMultipleEstudianteSerializer
# 
#     def perform_create(self, serializer):
#         pregunta = get_object_or_404(
#             Pregunta, id=self.request.data.get('preguntaSeleccionMultiple'))
#         return serializer.save(preguntaSeleccionMultiple=pregunta)
# 
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, *kwargs)
# 
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
# 
#
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


class RespuestaSleccionMultipleView(ListModelMixin, CreateModelMixin, GenericAPIView):
    # Add permissions to the view
    # permission_classes = [IsAuthenticated]

    # Add filter fields for the API
    filterset_fields = ("actividad",)
    # clase serializer para la transformacion de datos del request
    serializer_class = RespuestaSeleccionMultipleSerializer

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
# 
# 
# class RespMultipleView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     # Add permissions to the view
#     # permission_classes = [IsAuthenticated]
# 
#     # Add filter fields for the API
#     filterset_fields = ("preguntaSeleccionMultiple", "esCorrecta")
# 
#     # queryset usado para retornar los objetos requeridos
#     def get_queryset(self):
#         # Add filter to get all the answers of a desired student
#         preguntaSeleccionMultiple = self.request.query_params.get('preguntaSeleccionMultiple', None)
#         return Respuestmultiple.objects.filter(preguntaSeleccionMultiple=preguntaSeleccionMultiple)
# 
#     # clase serializer para la transformacion de datos del request
#     serializer_class = RespuestaMultipleSerializer
# 
#     def perform_create(self, serializer):
#         pregunta = get_object_or_404(
#             Pregunta, id=self.request.data.get('preguntaSeleccionMultiple'))
#         return serializer.save(preguntaSeleccionMultiple=pregunta)
# 
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, *kwargs)
# 
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
# 