from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from tasks.models import Task


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "tasks/index.html")


def show_tasks(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "tasks/tasks.html", context)


def add(request: HttpRequest) -> HttpResponse:
    pass


def remove(request: HttpRequest) -> HttpResponse:
    pass


def update(request: HttpRequest) -> HttpResponse:
    pass
