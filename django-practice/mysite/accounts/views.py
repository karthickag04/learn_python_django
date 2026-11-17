from django.shortcuts import redirect, render
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile


def login_view(request):

    #  if request.user.is_authenticated:
    #     return redirect('dashboard')

    if request.method == 'POST':

        form = LoginForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            # Get the user's profile
            profile = Profile.objects.get(user=user)

            # Role-based redirection
            if profile.role == 'student':

                return redirect('studentapp:index')

            elif profile.role == 'teacher':

                return redirect('teacherapp:index')

            elif profile.role == 'admin':

                return redirect('main:index')
        
        else:

            messages.error(
                request,
                'Invalid username or password'
            )

            
    else: 

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
                phone_number=form.cleaned_data['phone_number'],
                role=form.cleaned_data['role']
            )
            # return render(request, "accounts/login.html")
            return redirect("accounts:login")


    else:
        form = RegisterForm()
    
    
    return render(request, "accounts/register.html", {"form": form})


def change_password_view(request):
    return render(request, "accounts/change_password.html")


# Dashboard View
@login_required(login_url='accounts:login')
def dashboard(request):

    context = {
        'user': request.user
    }

    return render(
        request,
        'accounts/dashboard.html',
        context
    )

@login_required(login_url='accounts:login')
def logout_view(request):

    if request.method == 'POST':

        logout(request)

        return redirect('accounts:login')

    return redirect('accounts:dashboard')