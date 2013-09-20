import time

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import User, UserManager
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save, pre_save
from django.core.urlresolvers import reverse

from dazzle.apps.model.models import BaseModel, BaseModelManager

class DZUserManager(UserManager, BaseModelManager):
    def create_user(self, username, email, password, first_name, last_name):
        user = DZSiteUser(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=DZUser.ROLE_USER
        )
        user.set_password(password)
        user.save()

        return user

    def create_developer(self, username, email, password, first_name, last_name):
        dev = DZDeveloperUser(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=DZUser.ROLE_DEVELOPER
        )
        dev.set_password(password)
        dev.save()

        return dev

class DZUser(User, BaseModel):
    ROLE_USER = 'user'
    ROLE_DEVELOPER = 'developer'
    ROLE_CHOICES = (
        (ROLE_USER, 'Normal'),
        (ROLE_DEVELOPER, 'Developer'))

    role = models.CharField(max_length=60, choices=ROLE_CHOICES)
    last_active = models.DateTimeField(auto_now=False, null=True, blank=True)
    logged_in = models.BooleanField(default=False)

    user = DZUserManager()

    class Meta:
        app_label = 'accounts'


class DZSiteUser(DZUser):
    class Meta:
        proxy = True


class DZDeveloperUser(DZUser):
    class Meta:
        proxy = True

