from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('play/<int:pk>', views.Play.as_view(), name='play'),
    path('album/<int:pk>', views.album_detail, name='album-detail'),
    path('search/',views.Search.as_view(),name='search'),
    path('favorite/<int:songId>', views.add_or_remove_song_from_favorite, name='add-song-to-favorite')
]
