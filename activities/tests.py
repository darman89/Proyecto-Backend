from django.test import TestCase
from .models import PreguntaOpcionMultiple
import json
# Create your tests here.

class PreguntaTestCase(TestCase):

    def test_Get_Pregunta(self):
        url = '/pregunta/2'
        response = self.client.get(url, format='json' )
        self.assertEqual(response.status_code ,200)