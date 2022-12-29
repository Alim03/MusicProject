from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView
from .models import Artist, Song, Album
from account.models import Account
from django.http import HttpResponse


class Index(ListView):
    template_name = 'music/index.html'
    context_object_name = 'artists'
    model = Artist

    def get_queryset(self):
        query = super().get_queryset()
        return query[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songs'] = Song.objects.all().order_by('-id')[:3]
        context['albums'] = Album.objects.all().order_by('-id')[:3]
        return context


class Play(DetailView):
    template_name = 'music/player.html'
    model = Song


class AlbumDetail(DetailView):
    template_name = 'music/album_detail.html'
    context_object_name = 'album'
    model = Album

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        album = Album.objects.get(pk=id)
        context["songs"] = album.song_set.all()
        return context


def add_song_to_favorite(request, pk, songId):
    song = Song.objects.get(pk=songId)
    try:
        request.user.songs.get(pk=songId)
        request.user.songs.remove(song)
    except:
        request.user.songs.add(song)
    return HttpResponse()
