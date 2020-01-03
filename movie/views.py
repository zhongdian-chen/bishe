from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def films(request):
    return render(request, 'films.html')

def tab_desc(request):
    return render(request, 'tab_desc.html')

def tab_celebrity(request):
    return render(request, 'tab_celebrity.html')

def tab_img(request):
    return render(request, 'tab_img.html')