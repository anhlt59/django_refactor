from django.urls import reverse
from django.db import models
from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (
    AbstractBaseUser,
    UserManager as BaseUserManager, PermissionsMixin,
)

from ...core.db.fields import PositiveTinyIntegerField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, **extra_fields):
        """Create a user instance with the given email and password."""
        email = self.normalize_email(email)
        user = self.model(
            email=email, is_active=is_active, **extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(
            email, password, is_superuser=True, **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):

    class TYPES(models.IntegerChoices):
        STUDENT = 1
        COMPANY = 2
        ADMIN = 3

    username_validator = UnicodeUsernameValidator()

    type = PositiveTinyIntegerField("Type", choices=TYPES.choices, default=TYPES.STUDENT)
    username = models.CharField(
        "username", max_length=150, unique=True, blank=False,
        error_messages={"unique": settings.CONSTANTS.messages.USER_EXISTED,},
    )
    email = models.EmailField(
        "Email address", unique=True, blank=True,
        error_messages={"unique": settings.CONSTANTS.messages.EMAIL_EXISTED,},
    )
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "user"
        # swappable = "AUTH_USER_MODEL"
        indexes = [
            # models.Index(fields=["username", "password"], name="user_password_idx"),
            models.Index(fields=["username"], name="username_idx"),
        ]

    def __repr__(self):
        return f"{self.__class__.__name__}(type={self.type!r}, user={self.email!r})"

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        if not self.username:
            if self.email:
                # make User.username existed
                self.username = self.email
            else:
                raise ValueError("Model User missing username and email")

        super().save(*args, **kwargs)


# note: Student, Company, Admin proxy model, no table created
# STUDENT
# ------------------------------------------------------------------------------
class StudentManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.TYPES.STUDENT)


class Student(User):
    objects = StudentManager()

    class Meta:
        proxy = True


# COMPANY
# ------------------------------------------------------------------------------
class CompanyManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.TYPES.COMPANY)


class Company(User):
    objects = CompanyManager()

    class Meta:
        proxy = True


# Admin
# ------------------------------------------------------------------------------
class AdminManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.TYPES.ADMIN)


class Admin(User):
    objects = AdminManager()

    class Meta:
        proxy = True
