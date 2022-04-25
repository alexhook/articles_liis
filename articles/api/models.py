from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=50000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_private = models.BooleanField()