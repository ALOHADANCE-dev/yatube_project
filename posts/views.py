from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Главная страница
def index(request):
    return HttpResponse('Главная страница')

# Страница груп сообщества
def group_posts(requestk, pk):
    return HttpResponse('Лента новостей')