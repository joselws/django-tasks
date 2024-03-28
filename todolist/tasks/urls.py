from django.urls import path

from tasks import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/", views.show_tasks, name="show_tasks"),
    path("tasks/add", views.add, name="add"),
    path("tasks/edit/<int:task_id>", views.edit, name="edit"),
    path("tasks/delete/<int:task_id>", views.delete, name="delete"),
]
