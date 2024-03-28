from tasks.models import Task
from django.test import TestCase
from django.core.exceptions import ValidationError

# Create your tests here.

class TaskModelTestCase(TestCase):
    
    def test_task_created_correctly(self):
        """All task's given values are correctly set on creation"""

        task = Task.objects.create(title="simple task")

        self.assertEqual(task.title, "simple task")
        self.assertFalse(task.is_completed)
        self.assertEqual(len(Task.objects.all()), 1)
        self.assertEqual(task, Task.objects.all().first())

    def test_task_creation_error_missing_title(self):
        """
        Task raises ValidationError and is not created when the title attribute is not provided
        """
        task = Task()
        with self.assertRaises(ValidationError):
            task.full_clean()
            task.save()
        self.assertEqual(Task.objects.count(), 0)

    def test_task_creation_error_title_too_long(self):
        """
        Task raises ValidationError and is not created 
        when the title length exceeds 128 characters
        """
        # 129 characters' long title
        title = "a" * 129
        task = Task(title=title)
        with self.assertRaises(ValidationError):
            task.full_clean()
            task.save()
        self.assertEqual(Task.objects.count(), 0)
