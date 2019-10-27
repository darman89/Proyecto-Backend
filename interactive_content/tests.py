from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from users.models import Profesor


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