from django import forms
from dazzle.libs.fields import SubmitButtonField
from .fields import DropzoneField

class DZTemplateUploadForm(forms.Form):
    template_name = forms.CharField(max_length=50)
    dropzone = DropzoneField(label="Template Files") 
    submit = SubmitButtonField(label="", initial=u"Upload")

