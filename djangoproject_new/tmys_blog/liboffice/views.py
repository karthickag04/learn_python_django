from django.shortcuts import render

# Create your views here.

def lib_index(request):
    return render(request, "lib_index.html")

def catalog(request):
    # Logic to fetch catalog data (e.g., books)
    return render(request, 'catalog.html')


def membership(request):
    return render(request, "membership.html")

def book_borrowing(request):
    return render(request, "book_borrowing.html")

def library_events(request):
    return render(request, "library_events.html")

def contact_us(request):
    return render(request, "contact_us.html")