from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Artist
from django.http import HttpResponseRedirect
from django.urls import reverse
from shared.songs_utils import songs_and_is_liked_or_not


class AtristDetail(DetailView):
    template_name = 'artist/detail.html'
    context_object_name = 'artist'
    model = Artist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        artist = Artist.objects.get(pk=pk)
        context['albums'] = artist.album_set.all()
        songs = artist.song_set.all()[:5]
        songs = songs_and_is_liked_or_not(songs, self.request.user)
        context['songs'] = songs
        try:
            self.request.user.artists.get(pk=pk)
            favorite = 1
        except:
            favorite = 0

        context['favorite'] = favorite

        return context


class ArtistList(ListView):
    template_name = 'artist/all_artists.html'
    model = Artist
    paginate_by = 9


def add_or_remove_atrist_from_favorite(request, id):
    artist = Artist.objects.get(pk=id)
    try:
        request.user.artists.get(pk=id)
        request.user.artists.remove(artist)
    except:
        request.user.artists.add(artist)
    return HttpResponseRedirect(reverse('artist-detail', args=[id]))
