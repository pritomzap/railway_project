import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The email must be set"))
        if not password:
            raise ValueError(_("The password must be set"))
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        """Create and save a new superuser with given details"""
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 1)

        if extra_fields.get('role') != 1:
            raise ValueError('Superuser must have role of Global Admin')
        return self.create_user(email, password, **extra_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    MANAGER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee')
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    id = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier',primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=7)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=11)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.EmailField()
    modified_by = models.EmailField()

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        return self.first_name+" "+self.last_name

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

class RailwayPassenger(AbstractBaseUser):
    pnr = models.CharField(max_length=255, unique=True,primary_key=True)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    route_id = models.IntegerField()
    train_id = models.IntegerField()
    seat_amount = models.IntegerField()

    def get_pnr(self):
        return self.pnr
    def get_user_id(self):
        return self.user_id
    def get_route_id(self):
        return self.route_id
    def get_train_id(self):
        return self.train_id
    def get_seat_amount(self):
        return self.seat_amount

