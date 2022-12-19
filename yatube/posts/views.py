from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница')

def group_posts_list(request):
    return HttpResponse('Список постов')

def group_posts_detail(request, slug):
    return HttpResponse(f'Пост {slug}')