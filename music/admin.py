from django.contrib import admin
from .models import Album, Song, Genre


admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Genre)
