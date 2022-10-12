from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
# Главная страница
def index(request):
    return HttpResponse('Главная страница')

def group_posts(request, slug):
    return HttpResponse(f'Посты, {slug}')