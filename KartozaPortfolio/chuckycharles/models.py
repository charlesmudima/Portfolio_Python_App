from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy
# get text lazy to translate. Where i think data might be translated by the end user
# Responsible for us to mark the fields that database can be translated.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# django provides the permission mixing. Just hooking up the user to the permission of django
# Need to use the user manager if we are using the django default user model
# need create user and create super user

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        # check to make sure staff and superuser is set
        if other_fields.get('is_staff') is not True:
            raise ValueError(gettext_lazy('Superuser must be assigned to is_staff=True'))
        if other_fields.get('is_superuser') is not True:
            raise ValueError(gettext_lazy('Superuser must be assigned to is_superuser=True'))
        
        return self.create_user(email, user_name, first_name, last_name, password, **other_fields)
   
    def create_user(self, email, user_name, first_name, last_name, password, **other_fields):
        # validation check for the email
        if not email:
            raise ValueError(gettext_lazy('You must provide an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


# Create your models here.
class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(gettext_lazy('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    about = models.TextField(gettext_lazy('about'), max_length=500, blank=True)
    address = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name','last_name']

    def __str__(self):
        return self.user_name
