from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    user_name = 'Руслан'
    context = {'name':user_name}
    return render(request, 'homework/index.html', context)

