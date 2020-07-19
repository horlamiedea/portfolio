from django.shortcuts import render

def blog(request):
    
    return render(request, 'port/index.html')

def about(request):
    
    return render(request, 'port/about.html')

def contact(request):
    
    return render(request, 'port/contact.html')
