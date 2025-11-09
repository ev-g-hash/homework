from django.urls import path
from shop import views


urlpatterns = [
    path('', views.index, name='index'),       
    path('aboutas/', views.aboutas, name='aboutas'),       
    path('readmore/', views.readmore, name='readmore'), 
    path('forms/', views.forms, name='forms'),      
]