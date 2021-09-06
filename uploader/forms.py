from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from .models import File

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ('description', 'file')
        