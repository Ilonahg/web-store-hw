from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')
from django.shortcuts import render

# Create your views here.
