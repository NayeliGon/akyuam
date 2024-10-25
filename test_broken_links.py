from unittest import mock
from django.test import TestCase

# Aplica el mock a Twilio
with mock.patch.dict('sys.modules', {'twilio.rest': mock.MagicMock()}):
    from akyuamSystem.sistema import notificacion_boton  # Ahora importamos sin Twilio

class TestBrokenLinks(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)