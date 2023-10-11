from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView  # Import LoginView
from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    

class CustomLoginView(LoginView):  # Use Django's built-in LoginView
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')
    

def HomeView(request):
    # home page
    return render(request, 'home.html')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

