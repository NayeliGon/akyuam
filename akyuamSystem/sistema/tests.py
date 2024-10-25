from django.test import TestCase

# Create your tests here.
class SimpleTest(TestCase):
    def test_suma(self):
        self.assertEqual(1 + 1, 2)