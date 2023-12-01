from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name="tytuł", max_length=255)
    content = models.TextField(verbose_name="treść")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
