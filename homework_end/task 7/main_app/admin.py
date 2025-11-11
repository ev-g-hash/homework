from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age', 'phone', 'created_at']
    list_filter = ['created_at', 'age']
    search_fields = ['name', 'email']