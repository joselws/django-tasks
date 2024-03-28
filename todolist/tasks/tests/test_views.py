from django.test import Client
from django.test import TestCase


class TestIndexView(TestCase):
    def test_index_view(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.get("PATH_INFO"), "/")
        self.assertTemplateUsed(response, "tasks/index.html")
        self.assertTemplateUsed(response, "tasks/layout.html")
