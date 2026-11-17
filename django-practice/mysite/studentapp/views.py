from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from accounts.models import Profile



@login_required(login_url='accounts:login')
def index(request):

    profile = Profile.objects.get(user=request.user)
    context = {
        'user': request.user
    }
    if profile.role != 'student':
        raise PermissionDenied
    
    return render(
        request,
        'studentapp/index.html',
        context
    )