from django.test import Client
from django.test import TestCase
from tasks.models import Task
from django.urls import reverse


class TestIndexView(TestCase):
    def test_index_view(self):
        client = Client()
        response = client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.get("PATH_INFO"), "/")
        self.assertTemplateUsed(response, "tasks/index.html")
        self.assertTemplateUsed(response, "tasks/layout.html")


class TestShowTasksView(TestCase):
    def test_show_tasks_view(self):
        Task.objects.create(title="test task")
        Task.objects.create(title="test task2")
        client = Client()
        response = client.get(reverse("show_tasks"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.get("PATH_INFO"), "/tasks/")
        self.assertEqual(response.context.get("tasks").count(), 2)
        self.assertTemplateUsed(response, "tasks/tasks.html")
        self.assertTemplateUsed(response, "tasks/layout.html")

    def test_show_tasks_view_no_tasks(self):
        client = Client()
        response = client.get(reverse("show_tasks"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.get("PATH_INFO"), "/tasks/")
        self.assertEqual(response.context.get("tasks").count(), 0)
        self.assertTemplateUsed(response, "tasks/tasks.html")
        self.assertTemplateUsed(response, "tasks/layout.html")
