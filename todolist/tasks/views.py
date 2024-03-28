from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "tasks/index.html")


def tasks(request: HttpRequest) -> HttpResponse:
    pass


def add(request: HttpRequest) -> HttpResponse:
    pass


def remove(request: HttpRequest) -> HttpResponse:
    pass


def update(request: HttpRequest) -> HttpResponse:
    pass
