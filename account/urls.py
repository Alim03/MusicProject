from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('profile/', login_required(views.Index.as_view()), name='profile-index'),
    path('profile/update/<int:pk>', views.UpdateAccount.as_view(), name='update-account'),
    path('profile/change-password/<int:pk>', views.AccountChangePasswordView.as_view(), name='change-password'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile/songs/', views.FavoriteSongs.as_view(), name='favorite-songs'),
    path('profile/playlist/<int:pk>', views.PlayListView.as_view(), name='playlist'),
    path('profile/playlist/add', views.CreatePlaylist.as_view(), name='add-playlist'),
    path('profile/artists/', views.FavoriteArtists.as_view(), name='favorite-artists'),
    path('playlist/<int:pk>/delete/',views.DeletePlaylist.as_view(),name='delete-playlist'),
    path('playlist/update/<int:pk>/',views.UpdatePlaylist.as_view(),name='update-playlist'),
    path('playlist/<int:playlistid>/<int:songid>/delete/',views.delete_palylist_song,name='delete-playlist-song')
]
