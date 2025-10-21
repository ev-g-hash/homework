from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Index')
def aboutas(request):
    return HttpResponse('About')
