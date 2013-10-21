import time

from datetime import datetime, timedelta
from django.db import models
from django.utils.translation import ugettext_lazy as _

from dazzle.libs.model.models import BaseModel

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
    SESSION_TEMPLATE_ID = 'kSessionTemplateID'

    source = models.ForeignKey(
        DZTemplateSource,
        related_name='+',
        null=True,
        blank=True
    )

    template_name = models.TextField(default='')

    is_confirmed = models.BooleanField(_('is verified'), default=False,
        help_text='Designates whether this template was confirmed on upload')
    is_verified = models.BooleanField(_('is verified'), default=False,
        help_text='Designates whether this template was reviewed and verified')
    is_upload = models.BooleanField(_('is upload'), default=False,
        help_text='Designates whether this template was uploaded through our site '
                    'or a commit or manual entry.')

    class Meta:
        app_label = 'dashboard'

