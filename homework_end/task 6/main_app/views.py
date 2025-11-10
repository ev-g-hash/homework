from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from .models import User


# --- Отображение главной страницы (список пользователей) ---
def index(request):
    """
    Главная страница — список всех пользователей.
    """
    users = User.objects.all().order_by('id')
    return render(request, 'index.html', {
        'people': users  # как в вашем шаблоне — переменная people
    })


# --- Редактирование профиля ---
def edit_profile(request, id):
    try:
        profile_data = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponseNotFound(f"<h2>User profile with id={id} not found</h2>")

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        profile_data.name = name
        profile_data.age = age
        profile_data.phone = phone
        profile_data.email = email
        profile_data.save()

        return redirect('user_profile', id=id)

    else:
        return render(request, 'edit_profile.html', {
            'profile_data': profile_data
        })


# --- Профиль пользователя ---
def user_profile(request, id):
    profile_data = get_object_or_404(User, id=id)
    return render(request, 'user_profile.html', {
        'profile': profile_data
    })

def create_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age', None)
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')

        # Создаём нового пользователя
        user = User.objects.create(
            name=name,
            age=int(age) if age else None,
            phone=phone,
            email=email
        )
        return redirect('user_profile', id=user.id)

    return render(request, 'create_user.html')
