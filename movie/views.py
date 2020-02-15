from django.shortcuts import render
from movie import models
# Create your views here.

def main(request):
    return render(request, 'main.html')

def banner(request):
    return render(request, 'banner.html')

def layer(request):
    return render(request, 'layer.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def films(request):
    ret = models.FilmInfo.objects.get(id=1)
    return render(request, 'films.html', {"films_info": ret})

def tab_desc(request):
    return render(request, 'tab_desc.html')

def tab_celebrity(request):
    return render(request, 'tab_celebrity.html')

def tab_img(request):
    return render(request, 'tab_img.html')

def buy_ticket(request):
    ret = models.FilmInfo.objects.get(id=1)
    return render(request, 'buy_ticket.html', {"films_info": ret})

def select_seat(request):
    return render(request, 'select_seat.html')