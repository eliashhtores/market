from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, full_name, password, role, is_staff, is_superuser, is_active, **kwargs):
        role = kwargs.get('role', '0')
        user = self.model(
            email=email,
            full_name=full_name,
            role=role,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, full_name, password=None, role='0', **kwargs):
        return self._create_user(email, full_name, password, role, False, False, True, **kwargs)

    def create_superuser(self, email, full_name, password=None, role='0', **kwargs):
        return self._create_user(email, full_name, password, role, True, True, True, **kwargs)
