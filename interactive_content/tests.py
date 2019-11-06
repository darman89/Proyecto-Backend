import json

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.utils import json

from interactive_content.models import Contenido
from users.models import Profesor, Estudiante
from rest_framework.authtoken.models import Token


# Create your tests here.
class CreateInteractiveContentTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = Profesor.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)

    def test_add_interactive_content(self):
        url = '/content/cont_interactivo'
        interactive_content = {"nombre": "test", "contenido": "1"}
        self.client.force_login(user=self.user)
        contenido = Contenido.objects.create(url="test.com", nombre="contenido test", profesor_id=self.user.id)
        response = self.client.post(url, interactive_content, format='json',
                                    HTTP_AUTHORIZATION='Token ' + self.token.key)
        current_data = json.loads(response.content)
        self.assertEqual(current_data['nombre'], 'test')
        self.assertEqual(current_data['contenido']['id'], contenido.id)

    def test_unauthorized_user(self):
        url = '/content/cont_interactivo'
        estudiante = Estudiante.objects.create_user('estudiante', 'estudiante@admin.com', 'estudiante123')
        interactive_content = {"nombre": "test", "contenido": "1"}
        self.token = Token.objects.create(user=estudiante)
        self.client.force_login(user=estudiante)
        Contenido.objects.create(url="test.com", nombre="contenido test", profesor_id=self.user.id)
        response = self.client.post(url, interactive_content, format='json',
                                    HTTP_AUTHORIZATION='Token ' + self.token.key)
        current_data = json.loads(response.content)
        self.assertEqual(current_data['message'], 'Unauthorized')
        self.assertEqual(response.status_code, 401)


class InteractiveContentTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = Profesor.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)

    def test_lista_contenido_ok(self):
        url = '/content/content/'
        self.client.force_login(user=self.user)
        response = self.client.get(url, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.assertEqual(response.status_code, 200)

    def test_lista_contenido_un_elemento(self):
        url = '/content/content/'
        self.client.force_login(user=self.user)
        content = Contenido.objects.create(nombre="Contenido Prueba 1", url="https://youtube/test", profesor=self.user)
        response = self.client.get(url, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 1)
        self.assertEqual(current_data[0]['nombre'], content.nombre)

    def test_lista_contenido_dos_elementos(self):
        url = '/content/content/'
        self.client.force_login(user=self.user)
        content_1 = Contenido.objects.create(nombre="Contenido Prueba 2", url="https://youtube/test2",
                                             profesor=self.user)
        content_2 = Contenido.objects.create(nombre="Contenido Prueba 3", url="https://youtube/test3",
                                             profesor=self.user)
        response = self.client.get(url, format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 2)
        print(current_data)
        self.assertEqual(current_data[0]['nombre'], content_2.nombre)
        self.assertEqual(current_data[1]['nombre'], content_1.nombre)