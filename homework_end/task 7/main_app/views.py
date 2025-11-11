from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import UserProfile
from .forms import UserForm

def index(request):
    """Главная страница"""
    return render(request, 'index.html')

def user_list(request):
    """Список всех пользователей"""
    users = UserProfile.objects.all()
    return render(request, 'user_list.html', {'users': users})

def create_profile(request):
    """Создание нового профиля пользователя"""
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        else:
            # Ошибка валидации - временный редирект
            return redirect('user_list')
    else:
        # Метод GET - показать форму
        user_form = UserForm()
        return render(request, 'create_profile.html', {'user_form': user_form})

def add_user(request):
    """Добавить пользователя (альтернативный способ)"""
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        else:
            # Показать ошибки с той же формой
            return render(request, 'user_form.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'user_form.html', {'form': form})

def delete_user(request, user_id):
    """Удалить пользователя"""
    if request.method == 'POST':
        user = get_object_or_404(UserProfile, id=user_id)
        user.delete()
        return redirect('user_list')
    else:
        user = get_object_or_404(UserProfile, id=user_id)
        return render(request, 'confirm_delete.html', {'user': user})