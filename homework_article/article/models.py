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

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    description = models.TextField(max_length=255, blank=True, default='', verbose_name='описание')

    class Meta:                
        verbose_name = 'категорию'
        verbose_name_plural = 'категории' 

class Person(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='клиенты')
    last_name  = models.CharField(max_length=30, verbose_name='клиенты')

    class Meta:                
            verbose_name = 'клиентов'
            verbose_name_plural = 'клиенты' 