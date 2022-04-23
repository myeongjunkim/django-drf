from re import T
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    view_count = models.IntegerField(default=0)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)