from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "index/index.html")


def fft_sketch(request):
    return render(request, "fft_painter/index.html")


def weather(request):
    return render(request, "weather/index.html")


def markdown(request):
    return render(request, "markdown_editor/index.html")


def puzzle(request):
    return render(request, "puzzle/index.html")
