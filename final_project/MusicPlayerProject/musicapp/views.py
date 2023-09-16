# musicapp/views.py

from django.shortcuts import render, redirect
from .forms import SongUploadForm

def upload_song(request):
    if request.method == 'POST':
        form = SongUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page or wherever you want
    else:
        form = SongUploadForm()
    return render(request, 'upload_song.html', {'form': form})


# musicapp/views.py

from .models import Song

def home(request):
    songs = Song.objects.all()
    return render(request, 'home.html', {'songs': songs})


# musicapp/views.py

import requests
from django.http import JsonResponse

def get_spotify_track(request, track_id):
    # Use the Spotify Web API to fetch track details
    # Replace 'your_spotify_access_token' with your actual access token
    url = f'https://api.spotify.com/v1/tracks/{track_id}'
    headers = {'Authorization': 'Bearer your_spotify_access_token'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)

def get_soundcloud_track(request, track_id):
    # Use the SoundCloud API to fetch track details
    # Replace 'your_soundcloud_client_id' with your actual client ID
    url = f'https://api.soundcloud.com/tracks/{track_id}?client_id=your_soundcloud_client_id'
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)

from rest_framework import generics
from .models import Song
from .serializers import SongSerializer

class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

from pydub import AudioSegment
from pydub.playback import play

current_song = None  # To store the currently playing song

def play_song(request, song_id):
    global current_song
    song = Song.objects.get(pk=song_id)
    if current_song is not None:
        current_song.stop()  # Stop the currently playing song
    audio = AudioSegment.from_file(song.audio_file.path)
    play(audio)
    current_song = audio
    return JsonResponse({'status': 'playing'})

def pause_song(request):
    global current_song
    if current_song is not None:
        current_song.pause()
        return JsonResponse({'status': 'paused'})
    return JsonResponse({'status': 'no song playing'})

def stop_song(request):
    global current_song
    if current_song is not None:
        current_song.stop()
        current_song = None
    return JsonResponse({'status': 'stopped'})

# musicapp/views.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# musicapp/views.py

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'

# musicapp/views.py

from .forms import PlaylistForm

def create_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            return redirect('playlist_detail', playlist_id=playlist.id)
    else:
        form = PlaylistForm()
    return render(request, 'create_playlist.html', {'form': form})
