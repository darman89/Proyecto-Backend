from django.contrib import admin
from interactive_content.models import Curso
from users.models import Profesor

# Register your models here.
admin.site.register(Curso)
admin.site.register(Profesor)
