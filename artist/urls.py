from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>',views.AtristDetail.as_view(),name='artist-detail')
]
