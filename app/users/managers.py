import re

from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)  # pragma: no cover
        user.set_password(password)  # pragma: no cover
        user.save()  # pragma: no cover
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

    def normalize_email(self, email):
        """
        Normalize the email by lowercasing it and removing unwanted characters.
        """
        email = email.strip().lower()  # Normalize to lowercase and remove extra spaces
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValidationError(_("Invalid email address"))
        return email
