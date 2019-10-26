from django.test import TestCase
from datetime import datetime
from interactive_content.models import ContenidoInteractivo, Contenido, Curso
import json
from django.http import JsonResponse
from activities.models import Marca, PreguntaOpcionMultiple, Opcionmultiple, Calificacion
from users.models import Profesor, Estudiante
from rest_framework.utils import json
from django.contrib.auth.models import User, AbstractUser


# Create your tests here.

def escenario():
    profesor = Profesor(facultad="derecho",
                        direccion="cra 76#89-10",
                        telefono="1233322",
                        fecha_creacion=datetime.now(),
                        fecha_modificacion=datetime.now(),
                        username="Pablo123",
                        email="pablo@gmail.com",
                        password="qwertyu"
                        )
    profesor.save()

    contenido = Contenido(url="https://www.youtube.com/watch?v=FRivqBxbHRs",
                          nombre="video",
                          profesor=profesor
                          )
    contenido.save()

    curso = Curso(nombre="comunicacion",
                  descripcion="Desarrollar habilidades orales",
                  profesor=profesor
                  )
    curso.save()

    contenidoInteractivo = ContenidoInteractivo(contenido=contenido,
                                                tiene_retroalimentacion=True,
                                                tiempo_disponibilidad=datetime.now()
                                                )
    contenidoInteractivo.save()
    contenidoInteractivo.curso.add(curso)

    marca = Marca(nombre="marca1",
                  punto=33,
                  contenido=contenidoInteractivo
                  )
    marca.save()

class PreguntaTestCase(TestCase):



    def test_Get_Pregunta(self):


        escenario()
        marca = Marca.objects.get(nombre="marca1")


        pregunta = PreguntaOpcionMultiple()
        pregunta.nombre= "pregunta1"
        pregunta.enunciado="enunciado"
        pregunta.numeroDeIntentos = 1
        pregunta.tieneRetroalimentacion = True
        pregunta.esMultipleResp = True
        pregunta.marca_id = marca.id
        pregunta.save()

        print(str(pregunta.pk))
        print(str(pregunta.id))

        url = "/activities/preguntaOpcionMultiple"+ '/'+str(pregunta.pk)+'/'
        response = self.client.get(url, format='json' )
        print(response.context)
        self.assertEqual(response.status_code ,200)







class CalificacionCase(TestCase):
    def test_list_calificacion(self):
        url = '/activities/calificacion'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_count_calificaiones(self):
        profe = Profesor.objects.create(
            username='profe12', password='profe123', facultad='Ingenieria')
        contenido = Contenido.objects.create(
            url='www.ejemplo.com', nombre='Contenido', profesor=profe)
        cont_interac = ContenidoInteractivo.objects.create(
            contenido=contenido, tiene_retroalimentacion=False)
        marca = Marca.objects.create(
            nombre='marca', punto=7, contenido=cont_interac)
        pregunta = PreguntaOpcionMultiple.objects.create(
            enunciado='Pregunta 1', esMultipleResp=False, nombre='Actividad 1', numeroDeIntentos=3, tieneRetroalimentacion=True, marca=marca)
        opcion1 = Opcionmultiple.objects.create(
            opcion='A. Opcion1', esCorrecta=True, preguntaSeleccionMultiple=pregunta)
        estudiante1 = Estudiante.objects.create(
            username='esrudiante', password='estudiante123')
        estudiante2 = Estudiante.objects.create(
            username='esrudiant2', password='estudiante123')
        calificacion1 = Calificacion.objects.create(
            estudiante=estudiante1, actividad=pregunta, calificacion=4.5)
        calificacion2 = Calificacion.objects.create(
            estudiante=estudiante2, actividad=pregunta, calificacion=3.5)

        # url = '/activities/calificacion'
        # response = self.client.get(url, format='json')
        # current_data = json.loads(response.content)
        # self.assertEqual(len(current_data), 2)

    def test_filter_calificaiones_by_student(self):
        profe = Profesor.objects.create(
            username='profe12', password='profe123', facultad='Ingenieria')
        contenido = Contenido.objects.create(
            url='www.ejemplo.com', nombre='Contenido', profesor=profe)
        cont_interac = ContenidoInteractivo.objects.create(
            contenido=contenido, tiene_retroalimentacion=False)
        marca = Marca.objects.create(
            nombre='marca', punto=7, contenido=cont_interac)
        pregunta = PreguntaOpcionMultiple.objects.create(
            enunciado='Pregunta 1', esMultipleResp=False, nombre='Actividad 1', numeroDeIntentos=3, tieneRetroalimentacion=True, marca=marca)
        opcion1 = Opcionmultiple.objects.create(
            opcion='A. Opcion1', esCorrecta=True, preguntaSeleccionMultiple=pregunta)
        estudiante1 = Estudiante.objects.create(
            username='esrudiante', password='estudiante123')
        estudiante2 = Estudiante.objects.create(
            username='esrudiant2', password='estudiante123')
        calificacion1 = Calificacion.objects.create(
            estudiante=estudiante1, actividad=pregunta, calificacion=4.5)
        calificacion2 = Calificacion.objects.create(
            estudiante=estudiante2, actividad=pregunta, calificacion=3.5)

        url = '/activities/calificacion?estudiante=1'
        response = self.client.get(url, format='json')
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 1)

    def test_filter_calificaiones_by_question(self):
        profe = Profesor.objects.create(
            username='profe12', password='profe123', facultad='Ingenieria')
        contenido = Contenido.objects.create(
            url='www.ejemplo.com', nombre='Contenido', profesor=profe)
        cont_interac = ContenidoInteractivo.objects.create(
            contenido=contenido, tiene_retroalimentacion=False)
        marca = Marca.objects.create(
            nombre='marca', punto=7, contenido=cont_interac)
        pregunta = PreguntaOpcionMultiple.objects.create(
            enunciado='Pregunta 1', esMultipleResp=False, nombre='Actividad 1', numeroDeIntentos=3, tieneRetroalimentacion=True, marca=marca)
        pregunta2 = PreguntaOpcionMultiple.objects.create(
            enunciado='Pregunta 2', esMultipleResp=False, nombre='Actividad 2', numeroDeIntentos=1, tieneRetroalimentacion=True, marca=marca)
        opcion1 = Opcionmultiple.objects.create(
            opcion='A. Opcion1', esCorrecta=True, preguntaSeleccionMultiple=pregunta)
        estudiante1 = Estudiante.objects.create(
            username='esrudiante', password='estudiante123')
        estudiante2 = Estudiante.objects.create(
            username='esrudiante2', password='estudiante123')
        calificacion1 = Calificacion.objects.create(
            estudiante=estudiante1, actividad=pregunta, calificacion=4.5)
        calificacion2 = Calificacion.objects.create(
            estudiante=estudiante2, actividad=pregunta, calificacion=3.5)
        calificacion3 = Calificacion.objects.create(
            estudiante=estudiante1, actividad=pregunta2, calificacion=5.0)

        url = '/activities/calificacion?actividad=1'
        response = self.client.get(url, format='json')
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 1)

    def test_filter_obligatory(self):
        profe = Profesor.objects.create(
            username='profe12', password='profe123', facultad='Ingenieria')
        contenido = Contenido.objects.create(
            url='www.ejemplo.com', nombre='Contenido', profesor=profe)
        cont_interac = ContenidoInteractivo.objects.create(
            contenido=contenido, tiene_retroalimentacion=False)
        marca = Marca.objects.create(
            nombre='marca', punto=7, contenido=cont_interac)
        pregunta = PreguntaOpcionMultiple.objects.create(
            enunciado='Pregunta 1', esMultipleResp=False, nombre='Actividad 1', numeroDeIntentos=3, tieneRetroalimentacion=True, marca=marca)
        pregunta2 = PreguntaOpcionMultiple.objects.create(
            enunciado='Pregunta 2', esMultipleResp=False, nombre='Actividad 2', numeroDeIntentos=1, tieneRetroalimentacion=True, marca=marca)
        opcion1 = Opcionmultiple.objects.create(
            opcion='A. Opcion1', esCorrecta=True, preguntaSeleccionMultiple=pregunta)
        estudiante1 = Estudiante.objects.create(
            username='esrudiante', password='estudiante123')
        estudiante2 = Estudiante.objects.create(
            username='esrudiante2', password='estudiante123')
        calificacion1 = Calificacion.objects.create(
            estudiante=estudiante1, actividad=pregunta, calificacion=4.5)
        calificacion2 = Calificacion.objects.create(
            estudiante=estudiante2, actividad=pregunta, calificacion=3.5)
        calificacion3 = Calificacion.objects.create(
            estudiante=estudiante1, actividad=pregunta2, calificacion=5.0)

        url = '/activities/calificacion'
        response = self.client.get(url, format='json')
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 0)

    def test_create_calificacion(self):
        profe = Profesor.objects.create(
            username='profe12', password='profe123', facultad='Ingenieria')
        contenido = Contenido.objects.create(
            url='www.ejemplo.com', nombre='Contenido', profesor=profe)
        cont_interac = ContenidoInteractivo.objects.create(
            contenido=contenido, tiene_retroalimentacion=False)
        marca = Marca.objects.create(
            nombre='marca', punto=7, contenido=cont_interac)
        pregunta = PreguntaOpcionMultiple.objects.create(
            enunciado='Pregunta 1', esMultipleResp=False, nombre='Actividad 1', numeroDeIntentos=3, tieneRetroalimentacion=True, marca=marca)
        opcion1 = Opcionmultiple.objects.create(
            opcion='A. Opcion1', esCorrecta=True, preguntaSeleccionMultiple=pregunta)
        estudiante1 = Estudiante.objects.create(
            username='esrudiante', password='estudiante123')
        estudiante2 = Estudiante.objects.create(
            username='esrudiante2', password='estudiante123')

        url = '/activities/calificacion'
        data = JsonResponse(
            {"estudiante": "1", "actividad": "1", "calificacion": "3.7"})
        self.client.post(url, data)

        url = '/activities/calificacion?actividad=1'
        response = self.client.get(url, format='json')
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 1)

