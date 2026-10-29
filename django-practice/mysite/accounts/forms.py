
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Profile


class RegisterForm(UserCreationForm):

    email = forms.EmailField()
    address = forms.CharField(
        widget=forms.Textarea
    )
    phone_number = forms.CharField(
        max_length=15
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'address',
            'phone_number',
        ]
# Login Form
class LoginForm(AuthenticationForm):
    pass