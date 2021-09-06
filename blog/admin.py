from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'created_on')
    search_fields = ('title', 'author', 'content', 'tags', 'status')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 10
    summernote_fields = ('content',)