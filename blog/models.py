# from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICE = (
    (1, 'DRAFT'),
    (2, 'PUBLISHED')
)

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    tags = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICE, default=1)
