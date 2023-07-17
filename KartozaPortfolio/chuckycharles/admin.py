from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

class UserAdminConfig(UserAdmin):
    ordering = ['user_name']
    list_display = ('email','user_name','first_name', 'last_name', 'address', 'is_active', 'is_staff')
    
# Register your models here.
admin.site.register(Profile, UserAdminConfig)
