from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, TemplateView, CreateView, ListView, DetailView, DeleteView
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm, AuthenticationForm, PlaylistForm
from django.http import HttpResponseRedirect, HttpResponse
from artist.models import Artist
from music.models import Song
from account.models import Playlist


class Index(TemplateView):
    template_name = 'account/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songs'] = self.request.user.songs.order_by('-id').all()[:4]
        context['artists'] = self.request.user.artists.order_by(
            '-id').all()[:4]
        context['playlists'] = self.request.user.playlist_set.all().order_by(
            '-id').all()[:4]
        return context


class Register(View):

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=password)
            login(request, account)
            return redirect('index')

        return render(request, 'account/register.html', {'register_form': form})

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return redirect('index')

        form = RegistrationForm()
        return render(request, 'account/register.html', {'register_form': form})


class LogIn(View):

    def post(self, request):
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('index')
        return render(request, 'account/login.html', {'login_form': form})

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return redirect('index')

        form = AuthenticationForm()
        return render(request, 'account/login.html', {'login_form': form})


class FavoriteSongs(TemplateView):
    template_name = 'account/favorite_songs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songs'] = self.request.user.songs.all()
        return context


class CreatePlaylist(CreateView):
    template_name = 'account/create_playlist.html'
    success_url = '/account/profile'
    form_class = PlaylistForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class FavoriteArtists(ListView):
    template_name = 'artist/all_artists.html'
    model = Artist
    paginate_by = 9

    def get_queryset(self):
        query = super().get_queryset()
        query = self.request.user.artists.all()
        return query


class PlayListView(DetailView):
    template_name = 'account/user_playlist.html'
    model = Song

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        playlist = Playlist.objects.get(pk=id)
        context['album'] = playlist
        context["songs"] = playlist.song.all()
        return context


class DeletePlaylist(DeleteView):
    model = Playlist
    success_url = '/account/profile/'


def delete_palylist_song(request, playlistid, songid):
    playlist = Playlist.objects.get(pk=playlistid)
    song = Song.objects.get(pk=songid)
    playlist.song.remove(song)
    return HttpResponseRedirect(reverse('playlist', args=[playlistid]))


def logout_view(request):
    logout(request)
    return redirect('index')
