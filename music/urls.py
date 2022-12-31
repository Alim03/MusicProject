from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('play/<int:pk>', views.Play.as_view(), name='play'),
    path('album/<int:pk>', views.AlbumDetail.as_view(), name='album-detail'),
    path('favorite/<int:songId>', views.add_or_remove_song_from_favorite, name='add-song-to-favorite')
]
