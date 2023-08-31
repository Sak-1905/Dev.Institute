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
