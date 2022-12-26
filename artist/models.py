from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=500)
    image = models.ImageField(
        upload_to='images/', default=None, blank=True, null=True)
