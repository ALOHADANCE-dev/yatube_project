from django.shortcuts import render

# Create your views here.
# Главная страница
context = { 'index': 'Это главная страница проекта Yatube',
            'group_posts': 'Здесь будет информация о группах проекта Yatube'
}

def index(request):
    template = 'posts/index.html'
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    return render(request, template, context)