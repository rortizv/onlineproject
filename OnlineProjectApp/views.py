from django.shortcuts import render



def home(request):
    return render(request, 'OnlineProjectApp/home.html')


def store(request):
    return render(request, 'OnlineProjectApp/store.html')