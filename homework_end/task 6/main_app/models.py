from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=30)