from django.db import models
from artist.models import Artist


class Genre(models.Model):
    title = models.CharField(max_length=50)


class Album(models.Model):
    title = models.CharField(max_length=100)
    released_date = models.DateField()
    cover = models.ImageField(upload_to='images/')
    genre = models.ManyToManyField(Genre)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Song(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


