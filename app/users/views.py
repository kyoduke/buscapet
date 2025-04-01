from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, '_temp/login.html', {})

def register(request):
    return render(request, '_temp/register.html', {})