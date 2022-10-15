# posts/urls.py
from django.urls import path
from . import views
app_name = ' '

urlpatterns = [
    path('', views.index, name='start'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts')
]