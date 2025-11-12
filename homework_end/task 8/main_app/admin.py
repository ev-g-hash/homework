from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age', 'phone', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at', 'age']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at', 'updated_at']