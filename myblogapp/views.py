from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'font.html')

# def home(request):
#     return render(request, 'index.html')

def footer(request):
    return render(request, 'footer.html')

def form(request):
    return render(request, 'form.html')

def blogform(request):
    return render (request, 'blogform.html')

def nav(request):
    return render(request, 'nav/.html')

def contactpage(request):
    return render(request, 'contactpage.html')

