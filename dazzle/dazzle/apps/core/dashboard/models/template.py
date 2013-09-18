import time

from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save, pre_save
from django.core.urlresolvers import reverse

from dazzle.apps.model.models import BaseModel

class DZTemplate (BaseModel):
    class Meta:
        app_label = 'dashboard'
