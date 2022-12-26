from django.db import models
from music.models import Song, Album
from artist.models import Artist
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Usera must have an email address')
        if not username:
            raise ValueError('Usera must have a username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_profile_image_filepath(self, filename):
    return f''


def get_default_profile_image(self):
    return f''


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',
                              max_length=100, unique=True)
    username = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=300, upload_to=get_profile_image_filepath,
                                      null=True, blank=True, default=get_default_profile_image)

    objects = MyAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'username'

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        pass

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    song = models.ManyToManyField(Song)


class Review(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
