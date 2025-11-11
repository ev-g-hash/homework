from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_list/', views.user_list, name='user_list'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('add_user/', views.add_user, name='add_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
]