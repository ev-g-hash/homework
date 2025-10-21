from django.urls import path
from homework import views


urlpatterns = [
    path('', views.index), 
    path('aboutas/', views.aboutas),
]