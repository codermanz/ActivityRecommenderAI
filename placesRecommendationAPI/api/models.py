from django.db import models


# Create your models here.
class Suggestion(models.Model):
    url = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
