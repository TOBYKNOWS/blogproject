from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'nav.html')

