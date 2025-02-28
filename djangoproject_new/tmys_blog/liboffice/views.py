from django.shortcuts import render

# Create your views here.

def lib_index(request):
    return render(request, "lib_index.html")
