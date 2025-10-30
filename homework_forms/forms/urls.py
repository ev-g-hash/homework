from django.urls import path
from forms import views


urlpatterns = [
    path('', views.work1, name='work'), 
    path('work2/', views.work2, name='work2'),     
    path('work3/', views.work3, name='work3'),     
    path('work4/', views.work4, name='work4'),     
]
