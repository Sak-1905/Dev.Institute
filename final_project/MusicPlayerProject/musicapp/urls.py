# musicapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('upload/', views.upload_song, name='upload_song'),
]

# musicapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('', views.home, name='home'),
]


from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('api/songs/', views.SongListCreateView.as_view(), name='song-list-create'),
]

urlpatterns = [
    # Other URL patterns...
    path('api/songs/play/<int:song_id>/', views.play_song, name='play-song'),
    path('api/songs/pause/', views.pause_song, name='pause-song'),
    path('api/songs/stop/', views.stop_song, name='stop-song'),
]
# musicapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('create_playlist/', views.create_playlist, name='create_playlist'),
    # Add more URL patterns for editing and managing playlists
]

