from django.db import models
from django.contrib import admin
# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    title = models.CharField(max_length=255, unique=True)
    message = models.TextField(max_length=255)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'title')
    ordering = ('-id',)
    list_display_links = ('name', )
    search_fields = ('name', 'email', 'title', 'message')
    list_filter = ('name', 'email')

