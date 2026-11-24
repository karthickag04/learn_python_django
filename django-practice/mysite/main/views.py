from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.contrib import messages

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



# DELETE USER
@login_required(login_url='accounts:login')
def delete_user(request, user_id):

    profile = get_object_or_404(Profile, user=request.user)

    if profile.role != 'admin':
        raise PermissionDenied

    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':

        # Prevent admin from deleting their own account
        if user == request.user:
            messages.error(request, 'You cannot delete your own account!')
            return redirect('main:index')

        user.delete()

        messages.success(request, 'User deleted successfully!')

        return redirect('main:index')

    return redirect('main:index')