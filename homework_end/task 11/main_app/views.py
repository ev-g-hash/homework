from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from .models import User
from .forms import UserForm

def index(request):
    """Главная страница"""
    users_count = User.objects.count()
    return render(request, 'index.html', {'users_count': users_count})

def user_list(request):
    """Список всех пользователей"""
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def sort_users(request, field='id', dir='up'):
    """Сортировка пользователей по полю и направлению"""
    # Валидация параметра field
    valid_fields = ['id', 'name', 'age']
    if field not in valid_fields:
        field = 'id'
    
    # Валидация параметра dir
    valid_dirs = ['up', 'dn']
    if dir not in valid_dirs:
        dir = 'up'
    
    # Получение и сортировка записей
    users = User.objects.all()
    
    if dir == 'up':
        users = users.order_by(field)
        sort_direction = 'возрастанию'
    else:
        users = users.order_by(f'-{field}')
        sort_direction = 'убыванию'
    
    # Определение названия поля для отображения
    field_names = {
        'id': 'id',
        'name': 'имени',
        'age': 'возрасту'
    }
    sort_field_display = field_names.get(field, 'id')
    
    # Передача данных в шаблон
    context = {
        'user_data': users,
        'sort_field': sort_field_display,
        'sort_dir': sort_direction,
        'current_field': field,
        'current_dir': dir
    }
    
    return render(request, 'sort_users.html', context)

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