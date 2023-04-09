from django.shortcuts import render, redirect
from .forms import ContactForm
from db import email, password
from django.core.mail import EmailMessage


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            email = EmailMessage("Message from Django",
                "User {} with email {} sent the following message:\n\n {}".format(name, email, message),
                "",["rafael289@hotmail.com"])
            try:
                email.send()
                return redirect('/contact/?valid')
            except:
                return redirect('/contact/?novalid')
            
    return render(request, 'contact/contact.html', {'form': form})