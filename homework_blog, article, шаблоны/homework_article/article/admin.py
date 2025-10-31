from django.contrib import admin
from .models import Article, Group, Category, Person

admin.site.register(Article) 
admin.site.register(Group) 
admin.site.register(Category) 
admin.site.register(Person) 