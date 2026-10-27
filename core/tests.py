from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings


class FoundationTests(TestCase):
    """
    Verification tests for the initial platform architectural foundation.
    """

    def setUp(self):
        self.client = Client()

    def test_core_index_view(self):
        """Verify the home page loads successfully with base layout."""
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'Plastic Reimagined')
        self.assertContains(response, 'See Discarded Bottles as Canvases for Imagination')

    def test_destination_routes(self):
        """Verify all planned destination routes resolve and render properly."""
        routes = [
            ('studio:index', 'studio/index.html', 'Create — Studio'),
            ('catalogue:index', 'catalogue/index.html', 'Discover — Environmental Catalogue'),
            ('blog:index', 'blog/index.html', 'Read — Environmental Blog'),
            ('gallery:index', 'gallery/index.html', 'Gallery — Approved Creations'),
        ]
        for url_name, template_name, expected_text in routes:
            with self.subTest(url_name=url_name):
                response = self.client.get(reverse(url_name))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template_name)
                self.assertContains(response, expected_text)

    def test_admin_route_accessible(self):
        """Verify the Django administration site is registered and redirects to login."""
        response = self.client.get('/admin/')
        # Without authentication, Django admin redirects (302) to login URL
        self.assertEqual(response.status_code, 302)

    def test_database_configuration(self):
        """Verify database engine configuration."""
        db_config = settings.DATABASES['default']
        self.assertTrue('ENGINE' in db_config)
        self.assertTrue(len(db_config['ENGINE']) > 0)
