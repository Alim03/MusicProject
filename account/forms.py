from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, Playlist,Song
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Email is not valid')

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            clean_field = field.capitalize()
            if 'Password' in clean_field:
                clean_field = 'Password'
            self.fields[field].widget.attrs.update(
                {'class': 'form-control mb-4', 'placeholder': clean_field})

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.get(email=email)
        except:
            return email
        raise forms.ValidationError(f'Email {email} is taken.')

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.get(username=username)
        except:
            return username
        raise forms.ValidationError(f'Username {username} is taken.')


class AuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        update_form_field_attrs(self.fields)

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Wrong Email or Password')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email','username','profile_image')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        update_form_field_attrs(self.fields)


class ChangePasswordAccountForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control mb-4', 'placeholder': 'Old Password'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control mb-4', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control mb-4', 'placeholder': 'Repeat New Password'})

                

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ('name', 'cover')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control mb-4', 'placeholder': 'Name'})

def update_form_field_attrs(fields):
    for field in fields:
            fields[field].widget.attrs.update(
                {'class': 'form-control mb-4', 'placeholder': field.capitalize()})