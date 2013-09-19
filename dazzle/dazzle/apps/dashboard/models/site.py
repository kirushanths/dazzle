import time
from datetime import datetime, timedelta

from django.db import models

from dazzle.apps.model.models import BaseModel
from dazzle.apps.dashboard.models import DZTemplate
from dazzle.apps.accounts.models import DZUser

class DZSiteSettings (BaseModel):
    #any extra data per site basis

    class Meta:
        app_label = 'dashboard'


class DZSite (BaseModel):
    '''
    The main record of every dazzle site created.
    Try to keep minimal data in this model.
    Extras should be added to DZSiteSettings.
    '''

    #https://docs.djangoproject.com/en/dev/topics/db/queries/#following-relationships-backward
    created_by = models.ForeignKey(
        DZUser,
        related_name='+',
        null=True,
        blank=True
    )
    description = models.TextField(default='')
    settings = models.ForeignKey(DZSiteSettings)

    class Meta:
        app_label = 'dashboard'


class DZSiteCommit (DZTemplate):
    commited_by = models.ForeignKey(
        DZUser,
        related_name='commits',
        null=True,
        blank=True
    )
    site = models.ForeignKey(
        DZSite,
        related_name='commits',
        null=True,
        blank=True
    )
    class Meta:
        app_label = 'dashboard'


class DZSiteOwnership (BaseModel):
    REGULAR = 'regular'
    OBSERVING = 'observe'
    PENDING = 'pending'
    OWNERSHIP_TYPES = (
        REGULAR, 'Regular',
        OBSERVING, 'Observing',
        PENDING, 'Pending'
    )

    site = models.ForeignKey(
        DZSite,
        related_name='owners',
        null=True,
        blank=True
    )
    owner = models.ForeignKey(
        DZUser,
        related_name='sites',
        null=True,
        blank=True
    )

    ownership_type = models.CharField(max_length=100)

    class Meta:
        app_label = 'dashboard'
        unique_together = ('site', 'owner')

