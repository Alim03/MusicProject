from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm, AuthenticationForm
from .models import Account


class Index(TemplateView):
    template_name = 'account/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songs'] = self.request.user.songs.order_by('-id').all()[:4]
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
    


def logout_view(request):
    logout(request)
    return redirect('index')
