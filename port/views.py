from django.shortcuts import render

def blog(request):
    
    return render(request, 'port/index.html')
