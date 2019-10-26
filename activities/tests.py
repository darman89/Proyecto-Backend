from django.test import TestCase
from .models import PreguntaOpcionMultiple, Marca
from users.models import Profesor
from datetime import datetime
from interactive_content.models import ContenidoInteractivo, Contenido, Curso
import json
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