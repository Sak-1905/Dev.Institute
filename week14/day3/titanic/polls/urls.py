from django.urls import path 
from . import views

# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
    path('status', views.status, name='status'),
    path('about', views.about, name='about'),
    path('drivers', views.drivers, name='drivers'),
    path('test', views.test, name='test'),
]


# http://localhost:3000/polls/
# http://localhost:3000/polls/status
# http://localhost:3000/polls/about
# http://localhost:3000/polls/drivers
# http://localhost:3000/polls/test