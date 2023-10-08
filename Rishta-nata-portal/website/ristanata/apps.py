from django.apps import AppConfig


class RistanataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ristanata'

# urls.py
from django.urls import path
from .views import home, signup, login

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]
