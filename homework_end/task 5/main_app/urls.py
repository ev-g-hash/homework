from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('create/', views.create),    
    path('delete_profile/<int:id>/', views.delete_profile, name='delete_profile'),
    path('user_list/', views.user_list, name='user_list'),       
]


    
