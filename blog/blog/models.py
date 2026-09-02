from django.db import models

# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length=200)
    author = models.Charfield(max_length=200)
    body = models.TextField(200)

    def __str__(self):
        return self.title
