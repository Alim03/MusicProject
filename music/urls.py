from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('play/<int:pk>', views.Play.as_view(), name='play'),
    path('album/<int:pk>', views.AlbumDetail.as_view(), name='album-detail'),
    path('album/<int:pk>/<int:songId>',views.add_song_to_favorite,name='add-song-to-favorite')
]
