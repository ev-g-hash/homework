from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'shop/index.html')

def feedback(request):
    return render(request, 'shop/feedback.html')

def aboutas(request):
    return render(request, 'shop/aboutas.html')

def readmore(request):
    return render(request, 'shop/readmore.html')