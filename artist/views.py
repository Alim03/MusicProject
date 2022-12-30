from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Artist
from django.http import HttpResponseRedirect

class AtristDetail(DetailView):
    template_name = 'artist/detail.html'
    context_object_name = 'artist'
    model = Artist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        artist = Artist.objects.get(pk=pk)
        context['albums'] = artist.album_set.all()
        context['songs'] = artist.song_set.all()[:5]
        return context

class ArtistList(ListView):
    template_name='artist/all_artists.html'
    model=Artist
    paginate_by=9

def add_atrist_to_favorite(request, id):
    artist = Artist.objects.get(pk=id)
    try:
        request.user.artists.get(pk=id)
        request.user.artists.remove(artist)
    except:
        request.user.artists.add(artist)
    return HttpResponseRedirect('/')