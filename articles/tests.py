from django.test import TestCase


class TemplateTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_articles_page_status_code(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)

