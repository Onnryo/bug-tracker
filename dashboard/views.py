from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Hello, world!</h1>")


def about(request):
    return HttpResponse("<h1>About Page</h1>")
