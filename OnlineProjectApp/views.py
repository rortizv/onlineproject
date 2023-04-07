from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("This is home page")
    #return render(request, 'home.html')


def services(request):
    return HttpResponse("This is services page")
    # return render(request, 'services.html')


def store(request):
    return HttpResponse("This is store page")
    #return render(request, 'store.html')


def blog(request):
    return HttpResponse("This is blog page")
    # return render(request, 'blog.html')


def contact(request):
    return HttpResponse("This is contact page")
    # return render(request, 'contact.html')