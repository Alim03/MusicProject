from django.shortcuts import render, redirect
from django.views.generic import ListView, View, DetailView, CreateView
from .models import Artist, Song, Album
from django.http import HttpResponse, HttpResponseRedirect
from shared.songs_utils import songs_and_is_liked_or_not
from .forms import CommentForm
from account.models import Review
from django.urls import reverse
from itertools import chain



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

class Search(ListView):
    template_name='music/search.html'
    paginate_by=20
    count=0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context
    
    def get_queryset(self):
        request=self.request
        query=request.GET.get('q',None)
        if query is not None:
            albums=Album.objects.search(query)
            songs=Song.objects.search(query)
            artists=Artist.objects.search(query)

            query_chain=chain(albums,songs,artists)
            query_chain=list(query_chain)
            self.count=len(query_chain)
            return query_chain
            
        return Album.objects.none()
    
    
class Play(DetailView):
    template_name = 'music/player.html'
    model = Song


def album_detail(request, pk):
    template_name = 'music/album_detail.html'
    album = Album.objects.get(pk=pk)
    all_songs = album.song_set.all()
    comments = album.review_set.all().order_by('-date')
    songs = songs_and_is_liked_or_not(all_songs, request.user)
    if request.method == 'POST':
        post_dict = request.POST.copy() 
        form = CommentForm(post_dict)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.album = album
            new_comment.user = request.user
            new_comment.save()
            form = CommentForm()
            return render(request, template_name, 
            {'form': form, 'album': album, 'songs': songs, 'comments': comments})
    else:
        form = CommentForm()

    return render(request, template_name, 
    {'form': form, 'album': album, 'songs': songs, 'comments': comments})


def add_or_remove_song_from_favorite(request, songId):
    song = Song.objects.get(pk=songId)
    try:
        request.user.songs.get(pk=songId)
        request.user.songs.remove(song)
    except:
        request.user.songs.add(song)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
