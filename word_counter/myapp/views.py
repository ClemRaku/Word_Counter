from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
# Create your views here.

def counter(request):
    text = request.GET['text']#collecting the variable words from the index html
    amount_of_words = len(text.split())#basic python stuff to count words.
    return render(request, 'counter.html', {'amount' : amount_of_words}) #returning the amount_of_words via amount in the third parameter