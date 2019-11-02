from django.test import TestCase
from rest_framework.test import APIClient
from users.models import Profesor
from rest_framework.authtoken.models import Token
import json


# Create your tests here.
class CreateInteractiveContentTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = Profesor.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)

    def test_add_interactive_content(self):
        url = '/content/cont_interactivo'
        interactive_content = {"nombre": "test", "contenido_id": "1"}
        self.client.force_login(user=self.user)
        response = self.client.post(url, json.dumps(interactive_content), format='json', HTTP_AUTHORIZATION='Token ' + self.token.key)
        current_data = json.loads(response.content)
        self.assertEqual(current_data['nombre'], 'test')
        self.assertEqual(current_data['contenido_id'], '1')