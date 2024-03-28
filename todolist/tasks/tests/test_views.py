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


class TestAddTaskView(TestCase):
    def test_show_add_task_view(self):
        client = Client()
        response = client.get(reverse("add"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.get("PATH_INFO"), "/tasks/add")
        self.assertIsNone(response.context.get("message"))
        self.assertTemplateUsed(response, "tasks/add.html")
        self.assertTemplateUsed(response, "tasks/layout.html")

    def test_add_new_task_success(self):
        client = Client()
        data = {"title": "test title", "description": "lorem"}
        response = client.post(reverse("add"), data, follow=True)
        redirect_path, redirect_status_code = response.redirect_chain[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.get("PATH_INFO"), "/tasks/")
        self.assertEqual(redirect_path, "/tasks/")
        self.assertEqual(redirect_status_code, 302)
        self.assertIsNone(response.context.get("message"))
        self.assertTemplateUsed(response, "tasks/tasks.html")
        self.assertTemplateUsed(response, "tasks/layout.html")

    def test_add_new_task_error(self):
        client = Client()
        data = {"title": "", "description": "lorem"}
        response = client.post(reverse("add"), data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.request.get("PATH_INFO"), "/tasks/add")
        self.assertIsNotNone(response.context.get("message"))
        self.assertTemplateUsed(response, "tasks/add.html")
        self.assertTemplateUsed(response, "tasks/layout.html")


class TestEditView(TestCase):
    def test_successful_edit(self):
        client = Client()
        task = Task.objects.create(title="test task")
        response = client.post(reverse("edit", args=(task.id,)), follow=True)
        task.refresh_from_db()
        self.assertTrue(task.is_completed)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.get("PATH_INFO"), "/tasks/")
        self.assertTemplateUsed(response, "tasks/tasks.html")
        self.assertTemplateUsed(response, "tasks/layout.html")

    def test_unsuccessful_edit(self):
        client = Client()
        task = Task.objects.create(title="test task")
        response = client.post(reverse("edit", args=(task.id + 1,)), follow=True)
        task.refresh_from_db()
        self.assertFalse(task.is_completed)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.get("PATH_INFO"), "/tasks/")
        self.assertTemplateUsed(response, "tasks/tasks.html")
        self.assertTemplateUsed(response, "tasks/layout.html")


class TestDeleteView(TestCase):
    def test_successful_delete(self):
        client = Client()
        task = Task.objects.create(title="test task")
        response = client.post(reverse("delete", args=(task.id,)), follow=True)
        with self.assertRaises(Task.DoesNotExist):
            task.refresh_from_db()
        self.assertEqual(Task.objects.all().count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.get("PATH_INFO"), "/tasks/")
        self.assertTemplateUsed(response, "tasks/tasks.html")
        self.assertTemplateUsed(response, "tasks/layout.html")

    def test_unsuccessful_delete(self):
        client = Client()
        task = Task.objects.create(title="test task")
        response = client.post(reverse("delete", args=(task.id + 1,)), follow=True)
        task.refresh_from_db()
        self.assertEqual(Task.objects.all().count(), 1)
        self.assertFalse(task.is_completed)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.get("PATH_INFO"), "/tasks/")
        self.assertTemplateUsed(response, "tasks/tasks.html")
        self.assertTemplateUsed(response, "tasks/layout.html")
