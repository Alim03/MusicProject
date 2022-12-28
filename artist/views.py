from django.shortcuts import render
from django.views.generic import DetailView
from .models import Artist


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
