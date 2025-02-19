from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("Welcome to the main office!")
    return render(request, "index.html")


def services(request):
    # return HttpResponse("Welcome to the main office!")
    return render(request, "services.html")
