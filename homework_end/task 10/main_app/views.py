from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from .models import User
from .forms import UserForm

def index(request):
    """Главная страница"""
    return render(request, 'index.html')

def user_list(request):
    """Список всех пользователей"""
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def create_profile(request):
    """Создание нового профиля пользователя"""
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'success.html', {'user': user, 'action': 'created'})
        else:
            return render(request, 'create_profile.html', {'user_form': form})
    else:
        user_form = UserForm()
        return render(request, 'create_profile.html', {'user_form': user_form})

def edit_profile(request, user_id):
    """Редактирование профиля пользователя"""
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return HttpResponseNotFound('<h2>User profile with id={} not found</h2>'.format(user_id))
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile', user_id=user_id)
        else:
            return redirect('user_profile', user_id=user_id)
    else:
        user_form = UserForm(instance=user)
        return render(request, 'edit_profile.html', {'user_form': user_form, 'user': user})

def user_profile(request, user_id):
    """Просмотр профиля пользователя"""
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_profile.html', {'user': user})

def delete_user(request, user_id):
    """Удаление пользователя"""
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return redirect('user_list')
    else:
        user = get_object_or_404(User, id=user_id)
        return render(request, 'confirm_delete.html', {'user': user})