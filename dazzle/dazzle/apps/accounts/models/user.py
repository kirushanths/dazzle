import time

from datetime import datetime, timedelta

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save, pre_save
from django.core.urlresolvers import reverse

from dazzle.apps.model.models import BaseModel, BaseModelManager

class DZUserManager(BaseUserManager, BaseModelManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=DZUserManager.normalize_email(email),
            is_staff=False, is_active=True, is_superuser=False,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
 
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email,
            password=password,
            **extra_fields
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class DZUser(AbstractBaseUser, PermissionsMixin, BaseModel):
    ROLE_USER = 'user'
    ROLE_DEVELOPER = 'developer'
    ROLE_CHOICES = (
        (ROLE_USER, 'Normal'),
        (ROLE_DEVELOPER, 'Developer'))

    email = models.EmailField(max_length=254, unique=True, db_index=True)

    role = models.CharField(max_length=60, choices=ROLE_CHOICES, null=True, blank=True)

    first_name = models.CharField(_('first name'), max_length=50, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, null=True, blank=True)

    is_staff = models.BooleanField(_('is staff'), default=False,
        help_text='Designates whether the user can log into this admin '
                    'site.')
    is_active = models.BooleanField(_('is active'), default=True,
        help_text='Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')

    last_activity = models.DateTimeField(auto_now=False, null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    user = DZUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = 'accounts'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
 
    def get_short_name(self):
        return self.first_name

    def __unicode__(self):
        return self.email
 
    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True
 
    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True

