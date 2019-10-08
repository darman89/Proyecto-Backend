from django.db import models

from interactive_content.models import ContenidoInteractivo
from users.models import Estudiante

# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(max_length=30)
    punto = models.IntegerField(default=0)
    contenido = models.ForeignKey(ContenidoInteractivo, on_delete=models.CASCADE, related_name='marcas')


class Actividad(models.Model):
    nombre = models.CharField(max_length=30)
    numeroDeIntentos = models.IntegerField(default=0)
    tieneRetroalimentacion = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    calificacion = models.DecimalField(max_digits=10, decimal_places=2)
    retroalimentacion = models.CharField(max_length=200)

    def __str__(self):
        return self.calificacion


class Pregunta(models.Model):
    Pregunta = models.CharField(max_length=200)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)


class Respuestmultiple(models.Model):
    respuesta = models.CharField(max_length=200)
    esCorrecta = models.BooleanField()
    preguntaSeleccionMultiple = models.ForeignKey(Pregunta, on_delete=models.CASCADE)


class RespuestmultipleEstudiante(models.Model):
    seleccionada = models.BooleanField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    respuestmultiple = models.ForeignKey(Respuestmultiple, on_delete=models.CASCADE)


class RespuestaAbiertaEstudiante(models.Model):
    respuesta = models.CharField(max_length=200)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    preguntaAbierta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.respuesta


class RespuestaVoF(models.Model):
    esCorrecta = models.BooleanField()
    preguntaVoF = models.ForeignKey(Pregunta, on_delete=models.CASCADE)


class RespuestaEstudianteVoF(models.Model):
    respuesta = models.BooleanField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    preguntaVoF = models.ForeignKey(RespuestaVoF, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.respuesta
