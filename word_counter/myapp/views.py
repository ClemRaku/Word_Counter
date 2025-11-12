from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
# Create your views here.

def counter(request):
    return render(request, 'counter.html')