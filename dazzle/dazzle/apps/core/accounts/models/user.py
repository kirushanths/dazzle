import time

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import User, UserManager
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save, pre_save
from django.core.urlresolvers import reverse

from dazzle.apps.model.models import BaseModel

class DZUser(User, BaseModel):
    ROLE_USER = 'user'
    ROLE_DEVELOPER = 'developer'
    ROLE_CHOICES = (
        (ROLE_USER, 'Normal'),
        (ROLE_DEVELOPER, 'Developer'))

    role = models.CharField(max_length=60, choices=ROLE_CHOICES)
    last_active = models.DateTimeField(auto_now=False, null=True, blank=True)
    logged_in = models.BooleanField(default=False)

    class Meta:
        app_label = 'accounts'
