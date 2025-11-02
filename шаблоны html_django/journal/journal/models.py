from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    text = models.CharField(max_length=300, verbose_name='Заголовок')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Темы'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    text = models.TextField(verbose_name='Информация')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата')  

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.text[:50]}...'