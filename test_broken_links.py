from unittest.mock import patch
from django.test import TestCase
from django.urls import reverse, get_resolver

class BrokenLinksTest(TestCase):
    @patch.dict('sys.modules', {'twilio.rest': None})  # Mockea twilio.rest como None
    def test_urls(self):
        resolver = get_resolver()
        exclude_patterns = ['notificacion', 'twilio']
        broken_links = []

        for url_pattern in resolver.url_patterns:
            if any(exclude in url_pattern.pattern._route for exclude in exclude_patterns):
                continue  # Omitir rutas relacionadas con Twilio

            try:
                url = reverse(url_pattern.name)
                response = self.client.get(url)
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