import time

from datetime import datetime, timedelta

from dazzle.apps.model.models import BaseModel

class DZTemplate (BaseModel):
    class Meta:
        app_label = 'dashboard'
