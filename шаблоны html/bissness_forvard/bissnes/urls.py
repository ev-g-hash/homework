from django.urls import path
from bissnes import views


urlpatterns = [
    path('', views.index, name='index'),       
]