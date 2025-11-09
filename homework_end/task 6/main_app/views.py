from django.shortcuts import redirect, render 
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import User
from django.urls import reverse

def index(request):
    people = User.objects.all()    
    return render(request, 'main_app/index.html', {'people': people})

# Добавление данных
def create(request):
    if request.method == 'POST':
        user = User()
        user.name = request.POST.get('name')        
        user.age = request.POST.get('age')        
        user.phone = request.POST.get('phone')        
        user.email = request.POST.get('email')        
        user.save()
    return HttpResponseRedirect('/')



    