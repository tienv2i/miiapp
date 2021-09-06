from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.action(description='Mark as PUBLISHED')
def make_published(modeladmin, request, queryset):
    queryset.update(status=1)

@admin.action(description="Mark as DRAFT")
def make_draft(modeladmon, request, queryset):
    queryset.update(status=0)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'created_on')
    search_fields = ('title', 'author', 'content', 'tags', 'status')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 10
    summernote_fields = ('content',)
    actions = (make_published, make_draft, )
    list_filter = ('author', )
