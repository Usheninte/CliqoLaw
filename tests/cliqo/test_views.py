from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setup(self):
        self.client = Client()

    def test_home_view_GET(self):
        response = self.client.get(reverse('index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cliqo/home.html')

    def test_dashboard_view_GET(self):
        response = self.client.get(reverse('cliqo:dashboard'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cliqo/dashboard.html')
