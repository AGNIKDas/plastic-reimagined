from django.test import TestCase
from django.urls import reverse


class BlogViewTests(TestCase):
    def test_blog_index(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
