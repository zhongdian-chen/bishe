from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def welcome(request):
    return render(request, 'welcome.html')

def main(request):
    return render(request, 'main.html')