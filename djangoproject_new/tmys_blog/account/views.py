from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate



# Create your views here.


def base(request):
    return render(request, "base.html")

def register(request):
    if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                # login(request, user)  # Log the user in after registration
                return redirect('login_view')
    else:
        form = RegisterForm()

    
    return render(request, "register.html", {"form": form})



# User Login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
