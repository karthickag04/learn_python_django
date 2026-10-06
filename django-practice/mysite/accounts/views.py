from django.shortcuts import render
from .forms import RegisterForm, LoginForm


def login_view(request):
    form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def register_view(request):

    form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def change_password_view(request):
    return render(request, "accounts/change_password.html")