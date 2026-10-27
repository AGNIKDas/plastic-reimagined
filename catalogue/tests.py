from django.test import TestCase
from django.urls import reverse


class CatalogueViewTests(TestCase):
    def test_catalogue_index(self):
        response = self.client.get(reverse('catalogue:index'))
        self.assertEqual(response.status_code, 200)
