from django.urls import path
from ristana import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'), 
    path('signup/', views.RegisterView.as_view(), name='signup'),
]

