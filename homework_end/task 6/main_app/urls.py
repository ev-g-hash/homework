from django.urls import path
from . import views

app_name = 'main_app'  # Опционально: пространство имён

urlpatterns = [
    path('', views.index, name='index'),                    # Главная страница
    path('edit/<int:id>/', views.edit_profile, name='edit_profile'),
    path('user_profile/<int:id>/', views.user_profile, name='user_profile'),
    path('create/', views.create_user, name='create_user'),
]