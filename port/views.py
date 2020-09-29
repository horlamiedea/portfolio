from django.shortcuts import render
from django.contrib import messages
from my_port.settings import EMAIL_HOST_USER
from .models import Contact
from django.core.mail import send_mail

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
        subject = 'Thank you for reaching out to me'
        message = 'Hi, this is Olamide, to whatever you must have written I would send a reply to you soon. Thank you '
        recepient = email_r
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        messages.success(request, f'Your message was sent successfully, please be patient while I reply or connect with me via socia media')
        return render(request, 'port/contact.html')
    else:
        return render(request, 'port/contact.html')
