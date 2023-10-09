from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView  
from django.contrib.auth import login
from .forms import RegistrationForm
from .models import CustomUser  # Import your custom user model
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # Import AuthenticationForm
from .forms import LoginForm  # Import your LoginForm

class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    model = CustomUser  # Use your custom user model (CustomUser)

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            login(self.request, self.object)
            return response
        except Exception as e:
            # Log the error for debugging
            import logging
            logger = logging.getLogger(__name__)
            logger.error("Error in form_valid: %s" % str(e))
            return redirect('signup')

from django.contrib.auth.forms import AuthenticationForm  # Import AuthenticationForm

class CustomLoginView(LoginView):  
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')
    authentication_form = AuthenticationForm  # Use AuthenticationForm

    def form_valid(self, form):
        # Add debugging: print form data
        print("Form data:", form.cleaned_data)
        
        # Continue with the login process
        return super().form_valid(form)

    def form_invalid(self, form):
        # Add debugging: print form errors
        print("Form errors:", form.errors)
        
        # You can also add error messages for display
        messages.error(self.request, 'Login failed. Please check your credentials.')
        
        # Return to the login page with errors
        return self.render_to_response(self.get_context_data(form=form))



def home(request):
    return render(request, 'home.html')
