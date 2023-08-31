# musicapp/models.py

from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/')
    duration = models.FloatField()

    def __str__(self):
        return self.title

class Playlist(models.Model):
    title = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    play_count = models.PositiveIntegerField(default=0)
    last_played = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.song.title}"
