from django.db import models

# Create your models here.
from users.models import Profesor, Estudiante


class Curso(models.Model):
    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    nombre = models.CharField(max_length=255, blank=False, null=False)
    profesor = models.ForeignKey(Profesor, blank=False, null=False, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=255, blank=False, null=False)


class Contenido(models.Model):
    url = models.CharField(max_length=255, blank=False, null=False)
    nombre = models.CharField(max_length=255, blank=False, null=False)
    profesor = models.ForeignKey(Profesor, blank=False, null=False, on_delete=models.CASCADE)


class ContenidoInteractivo(models.Model):
    contenido = models.ForeignKey(Contenido, blank=False, null=False, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(null=False, auto_now_add=True)
    tiempo_disponibilidad = models.DateTimeField(null=True, blank=True)
    tiene_retroalimentacion = models.BooleanField()
    curso = models.ForeignKey(Curso, blank=False, null=False, on_delete=models.CASCADE)


class Grupo(models.Model):
    curso = models.ForeignKey(Curso, blank=False, null=False, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, blank=False, null=False, on_delete=models.CASCADE)


