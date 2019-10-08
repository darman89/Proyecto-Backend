# Register your models here.
from django.contrib import admin

from users.models import Usuario, Profesor, Estudiante

Models = [Usuario, Profesor, Estudiante]

admin.site.register(Models)
