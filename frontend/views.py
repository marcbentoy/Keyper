from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')


def keys(request):
    return render(request, 'frontend/keys.html')

def borrow(request):
    return render(request, 'frontend/borrow.html')

def history(request):
    return render(request, 'frontend/history.html')


def about(request):
    return render(request, 'frontend/about.html')

def handler404(request, exception):
    return render(request, 'frontend/404.html')