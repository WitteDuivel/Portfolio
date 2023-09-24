from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class MyProfileManager(BaseUserManager):
    pass


class Profile(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, primary_key=True)
    password = models.CharField(max_length=128)
    phone_number = PhoneNumberField(_("Phone number"), null=True, blank=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_state = models.CharField(max_length=50)
    address_country = models.CharField(max_length=50)

    professional_bio = models.TextField()
    # profile_pic = models.ImageField(upload_to="profile_pics", null=True, blank=True)
    skills = models.TextField()
    certificates = models.TextField()  # TODO

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_address(self):
        return f"{self.address_state}, {self.address_country}"

    objects = MyProfileManager()

    USERNAME_FIELD = "email"
