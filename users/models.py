from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class UserManager(BaseUserManager):

    def create_user(
            self,
            email,
            password=None,
            is_active=True,
            is_staff=False,
            is_admin=False
    ):
        if not email:
            raise ValueError("Email can't be empty")
        if not password:
            raise ValueError("Password can't be empty")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.set_password(password)
        user.save(using=self._db)
        return user

    def add_to_staff(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def make_admin(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user
