from django.shortcuts import render
from django.db.models import Q
import requests

from .models import Song


def index(request):
    allSongs = Song.objects.all().order_by('-last_updated')
    return render(request, template_name="index.html", context={"allSongs": allSongs})


def search_songs(request):
    template_path = 'search_result.html'

    search_query = request.GET.get('search', None)

    if search_query:
        search_result = Song.objects.filter(
            Q(songName__icontains=search_query) |
            Q(album__albumName__icontains=search_query) |
            Q(album__artist__artistName__icontains=search_query)
        ).distinct()
        spotify_tracks = spotify_api_search(search_query)

        context = {'search_result': search_result,
                   'search_query': search_query, 'spotify_tracks': spotify_tracks}
    else:
        search_result = Song.objects.all()
        context = {'search_result': search_result,
                   'search_query': search_query}
    return render(request, template_path, context)


def spotify_api_search(query):
    access_token = "BQDBKJ5eo5jxbtpWjVOj7ryS84khybFpP_lTqzV7uV-T_m0cTfwvdn5BnBSKPxKgEb11"
    endpoint = "https://api.spotify.com/v1/search"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    params = {
        "q": query,
        "type": "track",
    }
 # make a request to the spotify api
    response = requests.get(endpoint, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        tracks = data.get("tracks", {}).get("items", [])
    else:
        tracks = []
    return tracks