from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    ADMINISTRATOR = '0'
    WAREHOUSE = '1'
    SALES = '2'

    MALE = 'M'
    FEMALE = 'F'

    ROLE_CHOICES = [
        (ADMINISTRATOR, 'Administrator'),
        (WAREHOUSE, 'Warehouse'),
        (SALES, 'Sales')
    ]

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    # objects = UserManager()

    def get_email(self):
        return self.email

    def get_full_name(self):
        return self.full_name
