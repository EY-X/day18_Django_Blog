from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    draft = models.BooleanField(default=False)
    published_date = models.DateField()
    author = models.CharField(max_length=255)
