from django import forms
from .models import CustomUser  # Import your custom user model

class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Use your custom user model (CustomUser)
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Use your custom user model (CustomUser)
        fields = ['name', 'email', 'password', 'date', 'mru_phone_number', 'sex']
        widgets = {
            'password': forms.PasswordInput(),
        }