from django.forms import ModelForm
from .models import Attachment

class AttachmentForm(ModelForm):
    class Meta:
        model = Attachment
        fields = ('name', 'file')
        