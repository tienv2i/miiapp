from django.contrib import admin
from .models import ContactMessage
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'title')
    ordering = ('-id',)
    list_display_links = ('name', )
    search_fields = ('name', 'email', 'title', 'message')
    list_filter = ('name', 'email')
    list_per_page = 10
    summernote_fields = ('message',)
