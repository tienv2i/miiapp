from django.db.models.base import Model
from django.forms import ModelForm
from .models import ContactMessage

class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'title', 'message')