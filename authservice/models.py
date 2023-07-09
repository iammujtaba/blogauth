from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from authservice.manager import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True)
    email_verified_at = models.DateTimeField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    phone_number_verified_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = f'{self.first_name} {self.last_name}'

        return full_name.strip()
    
    @property
    def cleaned_name(self):
        return self.get_full_name()