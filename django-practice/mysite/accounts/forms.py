
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

    role = forms.ChoiceField(
        choices=Profile.ROLE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
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
            'role',
        ]
# Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(
    widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        }
    )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }
        )
    )

