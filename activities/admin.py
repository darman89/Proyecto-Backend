from django.contrib import admin
from activities.models import Actividad, Calificacion, Marca, RespuestaAbiertaEstudiante, RespuestaVoF, RespuestmultipleEstudiante

# Register your models here.

models = [Actividad, Calificacion, Marca, RespuestaAbiertaEstudiante, RespuestaVoF, RespuestmultipleEstudiante]

admin.site.register(models)
