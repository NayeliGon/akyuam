import requests
from django.test import TestCase
from django.urls import reverse, get_resolver

class BrokenLinksTest(TestCase):
   

    def test_urls(self):
        resolver = get_resolver()  # Obtiene todas las rutas configuradas en tu proyecto
        broken_links = []

        # Recorre todas las rutas encontradas
        for url_pattern in resolver.url_patterns:
            try:
                url = reverse(url_pattern.name)
                response = self.client.get(url)
                # Verifica si la respuesta es diferente a 200
                if response.status_code != 200:
                    broken_links.append((url, response.status_code))
            except Exception as e:
                broken_links.append((url_pattern.pattern, str(e)))

        if broken_links:
            print("Enlaces rotos detectados:")
            for link, error in broken_links:
                print(f"{link} -> {error}")
        else:
            print("No se encontraron enlaces rotos.")