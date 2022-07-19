from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!")

# def greet(request, name):
#     return HttpResponse(f"Hello, {name}!")

def greet1(request, name1):
    return HttpResponse(f"Hello; {name1.capitalize()}!")

def index2(request):
    return HttpResponse("<h1 style=\"color:blue\">Hello, world!</h1>")
