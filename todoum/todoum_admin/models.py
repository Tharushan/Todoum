from django.db import models


class Movie(models.Model):
    name: str = models.CharField(max_length=100, null=False, blank=False)
