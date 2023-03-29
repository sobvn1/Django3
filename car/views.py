from django.shortcuts import render
from .models import *

menu = ["о сайте", "Добавить статью", "Войти"]


def index(request):
    posts = Car.objects.all()
    return render(request, 'car/index.html', {"posts": posts, "menu": menu, "title": 'Главная информация'})


def about(request):
    return render(request, 'car/about.html')
