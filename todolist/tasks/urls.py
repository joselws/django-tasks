from django.urls import path

from tasks import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/", views.show_tasks, name="show_tasks"),
]
