from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hellooooo</h1>')
    return render(request,'index.html')

def count(request):
    text= request.GET['text']
    amount_of_word = len(text.split())
    return render(request,'count.html',{'amount':amount_of_word}) 