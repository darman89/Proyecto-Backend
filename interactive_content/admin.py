from django.contrib import admin
from interactive_content.models import Contenido, ContenidoInteractivo, Curso, Profesor
from activities.models import Actividad, Marca, Pregunta

# Register your models here.
admin.site.register(Contenido)
admin.site.register(ContenidoInteractivo)
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Actividad)
admin.site.register(Marca)
admin.site.register(Pregunta)
