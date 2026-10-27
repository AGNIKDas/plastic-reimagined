from django.test import TestCase
from django.urls import reverse


class GalleryViewTests(TestCase):
    def test_gallery_index(self):
        response = self.client.get(reverse('gallery:index'))
        self.assertEqual(response.status_code, 200)
