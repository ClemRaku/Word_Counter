from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
# Create your views here.

def counter(request):
    text = request.GET['text']#collecting the variable words from the index html
    return render(request, 'counter.html')