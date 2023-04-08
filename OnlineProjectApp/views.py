from django.shortcuts import render
from services.models import Service


def home(request):
    return render(request, 'OnlineProjectApp/home.html')


def services(request):
    # Get all services from the database
    services = Service.objects.all()
    return render(request, 'OnlineProjectApp/services.html', {'services': services})


def store(request):
    return render(request, 'OnlineProjectApp/store.html')


def blog(request):
    return render(request, 'OnlineProjectApp/blog.html')


def contact(request):
    return render(request, 'OnlineProjectApp/contact.html')