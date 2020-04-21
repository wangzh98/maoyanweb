from django.shortcuts import render
from .models import Movies
# Create your views here.


from django.http import HttpResponse

def savedata(request):
    return HttpResponse("Hello World！")

def index(request):
    return HttpResponse("Hello World！")

def home(request,home_id=1):
    home_idx = home_id
    movies = Movies.objects.all()[15*(home_idx-1):15*(home_idx)]
    if home_idx <= 1: #首页
        context = {'movies_list': movies, 'next_page': home_idx + 1, 'last_page': home_idx, 'cur_page': home_id}
    else:
        context = {'movies_list': movies, 'next_page': home_idx + 1, 'last_page': home_idx - 1, 'cur_page': home_id}
    return render(request, 'home.html', context)

def page(request,page_id):
    movie = Movies.objects.get(id=page_id)
    content = {'single_moive':movie}
    return render(request,'page.html', content)
