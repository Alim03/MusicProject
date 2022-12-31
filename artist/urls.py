from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtistList.as_view(), name='artists-list'),
    path('<int:pk>', views.AtristDetail.as_view(), name='artist-detail'),
    path('add/<int:id>',views.add_or_remove_atrist_from_favorite,name='add-atrist-to-favorite')
]
