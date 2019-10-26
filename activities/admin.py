from django.contrib import admin
from activities.models import Actividad, Calificacion, Marca, Respuesta,RespuestaVoF,RespuestaAbiertaEstudiante,RespuestmultipleEstudiante,Opcionmultiple, PreguntaOpcionMultiple,PreguntaAbierta, PreguntaFoV

# Register your models here.

models = [Actividad, Calificacion, Marca,PreguntaOpcionMultiple,Respuesta, RespuestaVoF , RespuestaAbiertaEstudiante,RespuestmultipleEstudiante,Opcionmultiple,PreguntaAbierta ,PreguntaFoV  ]
admin.site.register(models)
