from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,name,password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=11)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_mobile(self):
        return self.mobile

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def __str__(self):
        return self.email
