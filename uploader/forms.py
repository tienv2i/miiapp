from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Document

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document')
        