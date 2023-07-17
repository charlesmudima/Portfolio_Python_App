from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

# Listing, and display and searching of users in the admin panel
class UserAdminConfig(UserAdmin):
    ordering = ['user_name']
    list_display = ('email','user_name','first_name', 'last_name', 'address', 'is_active', 'is_staff')
    search_fields = ('email','user_name','first_name', 'last_name')
    list_filter = ('email','user_name','first_name', 'last_name', 'is_active', 'is_staff')
    
    fieldsets = (
        (None, {'fields': ('email','user_name','first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Personal', {'fields': ('about', 'phone_number','address')}),
    )
    # This is when you want to add a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','user_name','first_name', 'last_name', 'password1', 'password2', 'address','phone_number','is_active', 'is_staff')}
        ),
    )
# Register your models here.
admin.site.register(Profile, UserAdminConfig)
