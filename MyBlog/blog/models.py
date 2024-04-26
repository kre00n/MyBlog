from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField()
    author = models.TextField()
    heading = models.TextField()