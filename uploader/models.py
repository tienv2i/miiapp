from django.db import models
from django.contrib import admin

# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='document/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('uploaded_at', 'description', 'document')