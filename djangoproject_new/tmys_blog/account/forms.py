from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

# Registration Form
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Login Form
class LoginForm(AuthenticationForm):
    pass
