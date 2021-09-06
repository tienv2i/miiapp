# from enum import unique
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

STATUS_CHOICE = (
    (0, 'DRAFT'),
    (1, 'PUBLISHED')
)

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.URLField(blank=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    excerpt = models.TextField(null=True)
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)
    tags = TaggableManager()
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
