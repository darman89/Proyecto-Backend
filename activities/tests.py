from django.test import TestCase
from rest_framework.utils import json
from django.contrib.auth.models import User
import json

# Create your tests here.

class PortafolioTestCase(TestCase):
    def test_list_calificacion(self):
        url = '/activities/calificacion'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
