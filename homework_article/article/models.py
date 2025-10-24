from django.db import models

class Article(models.Model):
    title   = models.CharField(max_length=200, verbose_name='заголовок')
    date    = models.DateTimeField(verbose_name='дата')
    content = models.TextField(verbose_name='содержание')
    status  = models.IntegerField(verbose_name='статус')

    class Meta:                
        verbose_name = 'статьи'
        verbose_name_plural = 'статьи' 
    
class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL имя')
    description = models.TextField(verbose_name='Описание')

    class Meta:                
        verbose_name = 'группы'
        verbose_name_plural = 'группы' 