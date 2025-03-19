from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name=_("first name"), max_length=30)
    last_name = models.CharField(_("last name"), max_length=30, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True, db_index=True)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    objects = UserManager()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_deleted(self):
        return bool(self.deleted_at)

    def __str__(self):
        return self.email

    def soft_delete(self):
        if not self.deleted_at:
            self.deleted_at = timezone.now()
            self.save(update_fields=["deleted_at"])
