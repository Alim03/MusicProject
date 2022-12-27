from django.db import models
from artist.models import Artist


class Genre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=100)
    released_date = models.DateField()
    cover = models.ImageField(upload_to='images')
    genre = models.ManyToManyField(Genre)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='album')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
