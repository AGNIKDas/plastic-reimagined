from django.test import TestCase
from django.urls import reverse


class StudioViewTests(TestCase):
    def test_studio_index(self):
        response = self.client.get(reverse('studio:index'))
        self.assertEqual(response.status_code, 200)
