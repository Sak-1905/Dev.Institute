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
