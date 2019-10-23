from django.contrib import admin
from interactive_content.models import Contenido, ContenidoInteractivo, Curso, Profesor, Estudiante
from activities.models import Actividad, Marca

# Register your models here.
from interactive_content.models import Curso, Contenido, ContenidoInteractivo, Grupo

Models = [Curso, Contenido, ContenidoInteractivo, Grupo]

admin.site.register(Models)
