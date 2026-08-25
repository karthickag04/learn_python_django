from django.shortcuts import render


def login_view(request):
    return render(request, "accounts/login.html")


def register_view(request):
    return render(request, "accounts/register.html")


def change_password_view(request):
    return render(request, "accounts/change_password.html")