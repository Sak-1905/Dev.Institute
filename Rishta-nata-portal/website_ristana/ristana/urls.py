from django.urls import path
from ristana import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.CustomLoginView.as_view(), name='login'), 
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('home/', views.HomeView, name='home'),
]

