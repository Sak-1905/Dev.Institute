# views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'ristanata/signup.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'ristanata/login.html'
