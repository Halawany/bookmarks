from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    title = models.CharField(max_length=600)
    url = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title