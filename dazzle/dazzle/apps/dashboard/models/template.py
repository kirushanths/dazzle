import time

from datetime import datetime, timedelta
from django.db import models

from dazzle.apps.model.models import BaseModel

class DZTemplateSource (BaseModel):
    AMAZONS3 = 'amazons3'
    SOURCE_TYPES = (
        (AMAZONS3, 'Amazon S3'),
    )

    source_type = models.CharField(max_length=100, choices=SOURCE_TYPES)
    link = models.TextField(default='')

    class Meta:
        app_label = 'dashboard'


class DZTemplate (BaseModel):
    source = models.ForeignKey(
        DZTemplateSource,
        related_name='+',
        null=True,
        blank=True
    )
    class Meta:
        app_label = 'dashboard'

