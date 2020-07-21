from django.shortcuts import render
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
        return render(request, 'port/contact.html')
    else:
        return render(request, 'port/contact.html')
