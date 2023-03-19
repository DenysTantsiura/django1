from django.shortcuts import render

# Create your views here. # Почнемо з відображення
from django.http import HttpResponse  # спеціальний клас, який формує відповідь для клієнта.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")  # відповідь для клієнта "Hello, ..."
