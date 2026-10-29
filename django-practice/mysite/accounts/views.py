from django.shortcuts import redirect, render
from .forms import RegisterForm, LoginForm
from .models import Profile


def login_view(request):
    form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def register_view(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                address=form.cleaned_data['address'],
                phone_number=form.cleaned_data['phone_number']
            )
            # return render(request, "accounts/login.html")
            return redirect("accounts:login")


    else:
        form = RegisterForm()
    
    
    return render(request, "accounts/register.html", {"form": form})


def change_password_view(request):
    return render(request, "accounts/change_password.html")