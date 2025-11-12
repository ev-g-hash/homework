from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from django.urls import reverse
from .models import User
from .forms import UserForm

def index(request):
    """Главная страница"""
    return render(request, 'index.html')

def user_list(request):
    """Список всех пользователей"""
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_profile(request, user_id):
    """Просмотр профиля пользователя"""
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_profile.html', {'user': user})

def edit_profile(request, user_id):
    """Редактирование профиля пользователя"""
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Временный редирект в директорию профиля пользователя
            return redirect('user_profile', user_id=user_id)
        else:
            # При ошибке валидации - временный редирект
            return redirect('user_profile', user_id=user_id)
    else:
        # Метод не POST - показать форму с заполненными данными
        user_form = UserForm(instance=user)
        return render(request, 'edit_profile.html', {'user_form': user_form, 'user': user})

def add_user(request):
    """Добавить нового пользователя"""
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_profile', user_id=user.id)
        else:
            return render(request, 'user_form.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'user_form.html', {'form': form})

def delete_user(request, user_id):
    """Удалить пользователя"""
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return redirect('user_list')
    else:
        user = get_object_or_404(User, id=user_id)
        return render(request, 'confirm_delete.html', {'user': user})