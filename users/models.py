from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(
            self,
            email,
            password,
            is_active=True,
            is_staff=False,
            is_superuser=False
    ):
        if not email:
            raise ValueError("Email can't be empty")
        if not password:
            raise ValueError("Password can't be empty")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.active = is_active
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.set_password(password)
        user.save(using=self._db)
        return user

    def add_to_staff(self, email, password):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email
