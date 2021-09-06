import os
from django.db import models
from django.contrib import admin

# Create your models here.
class File(models.Model):
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='File/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
 
