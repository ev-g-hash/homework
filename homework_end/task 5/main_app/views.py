from django.shortcuts import get_object_or_404, redirect, render 
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import User, User1
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

# Удаление данных через GET - запрос    
def delete_profile(request, id):  
    try:
        user = User.objects.get(id=id)
        user.delete()        
        return redirect('user_list')
    except User.DoesNotExist:        
        return HttpResponseNotFound(f"<h2> User profile with {id} = принятый_id not found </h2>")

        
def user_list(request):       
    return render(request, 'main_app/user_list.html')   
    
  

    
    
 

    

