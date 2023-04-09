from django.shortcuts import render



def home(request):
    return render(request, 'OnlineProjectApp/home.html')





def store(request):
    return render(request, 'OnlineProjectApp/store.html')


def blog(request):
    return render(request, 'OnlineProjectApp/blog.html')


def contact(request):
    return render(request, 'OnlineProjectApp/contact.html')