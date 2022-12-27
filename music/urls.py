from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('play/<int:pk>', views.Play.as_view(), name='play'),
    path('album/<int:pk>', views.AlbumDetail.as_view(), name='album-detail')
]
