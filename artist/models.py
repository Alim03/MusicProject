from django.db import models
from django.db.models import Q

class ModelManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            lookup = (Q(name__icontains=query))
        qs=qs.filter(lookup).distinct().order_by('-id')
        return qs

class Artist(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=500)
    image = models.ImageField(
        upload_to='images', default=None, blank=True, null=True)

    objects= ModelManager()

    def __str__(self):
        return self.name