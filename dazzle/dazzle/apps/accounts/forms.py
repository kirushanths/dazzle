from django import forms
from .models import DZUser

class DZUserModelForm(forms.ModelForm):

    class Meta:
        model = DZUser