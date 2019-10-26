from django.test import TestCase
from .models import PreguntaOpcionMultiple, Marca, Opcionmultiple
from users.models import Profesor, Estudiante
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
                        username="Pablo123674",
                        email="pablo44@gmail.com",
                        password="qwer44tyu"
                        )
    profesor.id = 33333

    profesor.save()



    estudiante = Estudiante(codigo_de_estudiante="232223555",
                            direccion="cra 76#89-13",
                            telefono="1233323442",
                            fecha_creacion=datetime.now(),
                            fecha_modificacion=datetime.now(),
                            username="Andres1236222r",
                            email="andres222225@gmail.com",
                            password="qwer2222tyu"
                            )

    estudiante.id = 22333

    print(estudiante.id)
    estudiante.save()




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
    return marca


def escenario2():

    escenario()
    marca = escenario()


    pregunta = PreguntaOpcionMultiple()
    pregunta.nombre = "pregunta1"
    pregunta.enunciado = "enunciado"
    pregunta.numeroDeIntentos = 1
    pregunta.tieneRetroalimentacion = True
    pregunta.esMultipleResp = True
    pregunta.marca_id = marca.id
    pregunta.save()

    opcion = Opcionmultiple(opcion="opcion12",
                            esCorrecta=True,
                            preguntaSeleccionMultiple=pregunta)

    opcion.save()

    return opcion








class PreguntaTestCase(TestCase):



    def test_Get_Pregunta(self):



        marca = escenario()


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

class RespuestaSeleccionTestCase(TestCase):



    def test_guardar_Respuesta(self):



        opcion = escenario2()
        estudiante = Estudiante.objects.get(username="Andres1236222r")

        url = "/activities/respuestaOpcionMultiple/"

        response = self.client.post(url, {'respuestmultiple': opcion.id,
                                          'fecha_creacion': str(datetime.now()),
                                          'intento':2,
                                          'estudiante': 2
                                          })

        print(response.context)
        self.assertEqual(response.status_code ,200)


