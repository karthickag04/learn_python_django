from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("Welcome to the main office!")
    return render(request, "index.html")
