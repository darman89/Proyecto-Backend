from django.test import TestCase, Client
from .models import Contenido, ContenidoInteractivo, Curso
from datetime import datetime

from users.models import Profesor
from activities.models import Marca

import json

# Create your tests here.
class InteractiveContentTestCase(TestCase):

    url = '/content/interactivecontent/1'
    headers = {'Authorization': 'Token 452c39042e5e9874be461bbab2437a34a249014b', 'Content-Type': 'application/json'}

    def test_get_interactive_content_200_status(self):
        response = self.client.get(self.url, format='json', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_get_interactive_content_info(self):
        user = Profesor.objects.create(username="profesor.prueba", password="kda-qwerty-321", first_name="Profesor", last_name="Pruebas", email="a.acostag@uniandes.edu.co")

        content = Contenido.objects.create(url="youtube.com", nombre="Mi primer contenido", profesor=user)
        interactive_content = ContenidoInteractivo.objects.create(contenido=content, fecha_creacion=datetime.now(), tiene_retroalimentacion=True)
        response = self.client.get(self.url, format='json', headers=self.headers)
        data = json.loads(response.content)

        self.assertEqual(data[0]['fields']['nombre'], content.nombre)
        self.assertEqual(data[0]['fields']['tieneRetroalimentacion'], interactive_content.tiene_retroalimentacion)
        self.assertEqual(data[0]['fields']['contenido']['nombre'], content.nombre)
        self.assertEqual(data[0]['fields']['contenido']['url'], content.url)

    def test_get_courses_from_interactive_content(self):
        user = Profesor.objects.create(username="profesor.prueba", password="kda-qwerty-321", first_name="Profesor", last_name="Pruebas", email="a.acostag@uniandes.edu.co")

        content = Contenido.objects.create(url="youtube.com", nombre="Mi primer contenido", profesor=user)
        interactive_content = ContenidoInteractivo.objects.create(contenido=content, fecha_creacion=datetime.now(), tiene_retroalimentacion=True)

        curso1 = Curso.objects.create(fecha_creacion=datetime.now(), nombre="Mi primer curso", profesor=user, descripcion="Breve descripcion 1")
        curso2 = Curso.objects.create(fecha_creacion=datetime.now(), nombre="Mi segundo curso", profesor=user, descripcion="Breve descripcion 2")

        interactive_content = ContenidoInteractivo.objects.create(contenido=content, fecha_creacion=datetime.now(),
                                                                  tiene_retroalimentacion=True)
        interactive_content.curso.add(curso1)
        interactive_content.curso.add(curso2)

        response = self.client.get(self.url, format='json', headers=self.headers)
        data = json.loads(response.content)

        self.assertEqual(data[0]['fields']['cursos'][0]['nombre'], interactive_content.curso.first().nombre)
        self.assertEqual(data[0]['fields']['cursos'][1]['nombre'], interactive_content.curso.last().nombre)
        self.assertEqual(data[0]['fields']['cursos'][0]['descripcion'], interactive_content.curso.first().descripcion)
        self.assertEqual(data[0]['fields']['cursos'][1]['descripcion'], interactive_content.curso.last().descripcion)

    def test_get_marcas_from_interactive_content(self):
        user = Profesor.objects.create(username="profesor.prueba", password="kda-qwerty-321", first_name="Profesor", last_name="Pruebas", email="a.acostag@uniandes.edu.co")

        content = Contenido.objects.create(url="youtube.com", nombre="Mi primer contenido", profesor=user)
        interactive_content = ContenidoInteractivo.objects.create(contenido=content, fecha_creacion=datetime.now(), tiene_retroalimentacion=True)

        marca1 = Marca.objects.create(nombre="Marca 1", punto=100, contenido=interactive_content)
        marca2 = Marca.objects.create(nombre="Marca 2", punto=200, contenido=interactive_content)

        response = self.client.get(self.url, format='json', headers=self.headers)
        data = json.loads(response.content)

        self.assertEqual(data[0]['fields']['marcas'][0]['id'], 1)
        self.assertEqual(data[0]['fields']['marcas'][0]['punto'], marca1.punto)
        self.assertEqual(data[0]['fields']['cursos'][1]['id'], 2)
        self.assertEqual(data[0]['fields']['cursos'][1]['punto'], marca2.punto)
