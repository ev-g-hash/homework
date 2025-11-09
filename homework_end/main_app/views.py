from django.shortcuts import get_object_or_404, redirect, render 
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
        user.save()
    return HttpResponseRedirect('/')

# Изменение данных
def edit(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponseNotFound(f"User profile with not found")

    if request.method == 'POST':        
        user.name = request.POST.get('name')
        user.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, 'main_app/edit.html', {'user': user}) 

# Удаление данных
def delete(request, id):
    user = User.objects.get(id=id)
   
    try:
        if request.method == 'POST': 
            user.id = request.POST.get('name')
            user.delete()        
            return HttpResponseRedirect("/")
        else:
             return render(request, 'main_app/user_list.html', {'user': user}) 
    
    except Exception as e:        
        return render(request, 'main_app/user_list2.html')
    
    
        
    
    
    
       
    
    
    

