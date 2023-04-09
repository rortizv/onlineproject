from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            return redirect('/contact/?valid')
            
    return render(request, 'contact/contact.html', {'form': form})