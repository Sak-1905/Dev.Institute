from django.shortcuts import render
from .models import Song, Playlist

def browse_songs(request):
    songs = Song.objects.all()
    return render(request, 'musicapp/browse_songs.html', {'songs': songs})

def create_playlist(request):
    if request.method == 'POST':
        # Process form data to create a new playlist
        # ...
        return redirect('playlist-list')  # Redirect to playlist listing page
    return render(request, 'musicapp/create_playlist.html')
