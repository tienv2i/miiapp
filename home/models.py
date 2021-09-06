from django.db import models
from django.contrib import admin
from django_quill.fields import QuillField
# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    title = models.CharField(max_length=255, unique=True)
    message = models.TextField()

