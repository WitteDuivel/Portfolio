from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyProfileManager(BaseUserManager):
    pass

class Profile(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, primary_key=True)
    password = models.CharField(max_length=128)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    objects = MyProfileManager()

    USERNAME_FIELD = 'email'