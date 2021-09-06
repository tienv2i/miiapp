from django.contrib import admin
from .models import File
# Register your models here.

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('uploaded_at', 'description', 'file')
    list_per_page = 10
    search_fields = ('description', 'file__name')