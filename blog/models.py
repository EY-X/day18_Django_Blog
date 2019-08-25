from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(validators=[MinLengthValidator(1)])
    draft = models.BooleanField(default=False)
    published_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=255)
    