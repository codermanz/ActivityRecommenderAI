from django.db import models


# Create your models here.
class Suggestion(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=100)
    description = models.TextField()
