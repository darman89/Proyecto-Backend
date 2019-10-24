from django.contrib import admin
from activities.models import Actividad, Calificacion, Marca, Pregunta, RespuestaAbiertaEstudiante, RespuestaVoF, Respuestmultiple, RespuestaEstudianteVoF, RespuestmultipleEstudiante

# Register your models here.

models = [Actividad, Calificacion, Marca, Pregunta, RespuestaAbiertaEstudiante, RespuestaVoF, Respuestmultiple, RespuestaEstudianteVoF, RespuestmultipleEstudiante]

admin.site.register(models)
