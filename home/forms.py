from django.db.models.base import Model
from django.forms import ModelForm, widgets
from .models import ContactMessage
from django_summernote.widgets import SummernoteWidget

class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        widgets = {
            'message': SummernoteWidget()
        }
        fields = ('name', 'email', 'title', 'message')