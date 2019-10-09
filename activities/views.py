from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from users.models import Profesor
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers

from .models import Marca, Actividad, Pregunta, RespuestaEstudianteVoF, RespuestmultipleEstudiante, Respuestmultiple, RespuestaVoF

# Create your views here.
@csrf_exempt
def reports(request):

    #TODO: Get correct professor through token or session
    get_the_professor = Profesor.objects.first()

    big_json = {}
    big_json['username'] = get_the_professor.username
    big_json['first_name'] = get_the_professor.first_name
    big_json['last_name'] = get_the_professor.last_name
    big_json['email'] = get_the_professor.email
    big_json['direccion'] = get_the_professor.direccion
    big_json['telefono'] = get_the_professor.telefono
    big_json['facultad'] = get_the_professor.facultad
    big_json['marcas'] = []

    marcas = Marca.objects.filter(contenido__contenido__profesor=get_the_professor)
    for marca in marcas:

        big_json['marcas'].append({'nombre':marca.nombre,'actividades':[]})
        actividades = Actividad.objects.filter(marca=marca)

        for actividad in actividades:

            big_json['marcas'][-1]['actividades'].append({'nombre':actividad.nombre, 'preguntas':[]})
            preguntas = Pregunta.objects.filter(actividad=actividad)

            for pregunta in preguntas:

                big_json['marcas'][-1]['actividades'][-1]['preguntas'].append({'pregunta':pregunta.Pregunta, 'tipo':'', 'opciones':[]})
                opciones = Respuestmultiple.objects.filter(preguntaSeleccionMultiple=pregunta)

                if opciones.count() != 0:
                    big_json['marcas'][-1]['actividades'][-1]['preguntas'][-1]['tipo'] = 'multiple'
                    for opcion in opciones:
                        votos = RespuestmultipleEstudiante.objects.filter(respuestmultiple=opcion).count()
                        big_json['marcas'][-1]['actividades'][-1]['preguntas'][-1]['opciones'].append({'respuesta':opcion.respuesta, 'esCorrecta': opcion.esCorrecta, 'votos':votos})
                else:
                    big_json['marcas'][-1]['actividades'][-1]['preguntas'][-1]['tipo'] = 'verdadero/falso'
                    VF = RespuestaVoF.objects.filter(preguntaVoF=pregunta)
                    for vf in VF:
                        isCorrect = vf.esCorrecta
                        howManyTrue = RespuestaEstudianteVoF.objects.filter(preguntaVoF=vf, respuesta=True).count() #"howTrue":value
                        howManyFalse = RespuestaEstudianteVoF.objects.filter(preguntaVoF=vf, respuesta=False).count() #"howFalse":value
                        big_json['marcas'][-1]['actividades'][-1]['preguntas'][-1]['opciones'].append(
                            {'respuesta': vf.esCorrecta, 'numeroVerdadero': howManyTrue, 'numeroFalso': howManyFalse})

    return JsonResponse(big_json)
