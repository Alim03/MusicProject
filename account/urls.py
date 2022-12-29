from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.Index.as_view(), name='profile-index'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),
]
