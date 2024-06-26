from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.urls import reverse
from tasks.models import Task


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "tasks/index.html")


def show_tasks(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "tasks/tasks.html", context)


def add(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "tasks/add.html")

    # Handle form submission (request.method == "POST")
    title = request.POST.get("title")
    description = request.POST.get("description")
    task = Task(title=title, description=description)

    try:
        task.full_clean()
        task.save()
    except ValidationError:
        # Redirect to add.html with an error message
        context = {"message": "Task title validation error"}
        return render(request, "tasks/add.html", context, status=400)

    return HttpResponseRedirect(reverse("show_tasks"))


def delete(request: HttpRequest, task_id: int) -> HttpResponse:
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return HttpResponseRedirect(reverse("show_tasks"))

    task.delete()
    return HttpResponseRedirect(reverse("show_tasks"))


def edit(request: HttpRequest, task_id: int) -> HttpResponse:
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return HttpResponseRedirect(reverse("show_tasks"))

    task.is_completed = not task.is_completed
    task.save()
    return HttpResponseRedirect(reverse("show_tasks"))
