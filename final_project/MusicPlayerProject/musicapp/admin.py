# musicapp/admin.py

from django.contrib import admin
from .models import Song, Playlist, UserInteraction

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(UserInteraction)
