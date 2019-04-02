from django.test import TestCase


class TemplateTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_articles_page_status_code(self):
        uuid = "f52c15f2-c5a9-11e7-8889-0050569d4be0"
        response = self.client.get(f'/article/{uuid}')
        self.assertEqual(response.status_code, 200)
