# from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICE = (
    (0, 'DRAFT'),
    (1, 'PUBLISHED')
)

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.URLField(blank=True)
    tags = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)
