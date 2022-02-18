from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, full_name, password, is_staff, is_superuser, **kwargs):
        user = self.model(
            email=email,
            full_name=full_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, full_name, password=None, **kwargs):
        return self._create_user(email, full_name, password, False, False, **kwargs)

    def create_superuser(self, email, full_name, password=None, **kwargs):
        return self._create_user(email, full_name, password, True, True, **kwargs)
