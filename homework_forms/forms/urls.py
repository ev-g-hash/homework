from django.urls import path
from forms import views


urlpatterns = [
    path('', views.work1, name='work'), 
    path('work2/', views.work2, name='work2'),     
    path('work3/', views.work3, name='work3'),     
    path('work4/', views.work4, name='work4'),     
    path('work5/', views.work5, name='work5'),     
    path('work6/', views.work6, name='work6'),   
]
