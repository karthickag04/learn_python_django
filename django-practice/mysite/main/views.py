from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

from accounts.models import Profile

# Create your views here.


@login_required(login_url='accounts:login')
def index(request):

    profile = Profile.objects.get(user=request.user)
  



    if profile.role != 'admin':
            raise PermissionDenied


     # Fetch all users from the database
    users = User.objects.all().select_related('profile')
    context = {
            'users': users
        }


    return render(request, "main/index.html",context)
