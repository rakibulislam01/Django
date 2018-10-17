from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def pools(request):
    return HttpResponse("Hello")


def home_view(request):
    return HttpResponse("hi")
