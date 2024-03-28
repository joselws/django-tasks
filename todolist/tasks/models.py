from django.db import models


# Create your models here.
class Task(models.Model):
    """
    Task model with the following attributes:
        title - CharField(128)
        description - TextField(1024, blank=True)
        is_completed - BooleanField(default=False)
    """

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1024, blank=True)
    is_completed = models.BooleanField(default=False)

    def __repr__(self) -> str:
        return f"Task ({self.pk}): {self.title}"

    def __str__(self) -> str:
        return f"Task ({self.pk}): {self.title}"
