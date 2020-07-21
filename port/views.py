from django.shortcuts import render
from django.contrib import messages
from .models import Contact

def blog(request):
    
    return render(request, 'port/index.html')

def about(request):
    
    return render(request, 'port/about.html')

def contact(request):
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        message_r = request.POST.get('message')

        c = Contact(name=name_r, email=email_r, message=message_r)
        c.save()
        messages.success(request, f'Your message was sent successfully, please be patient while I reply or connect with me via socia media')
        return render(request, 'port/contact.html')
    else:
        return render(request, 'port/contact.html')
