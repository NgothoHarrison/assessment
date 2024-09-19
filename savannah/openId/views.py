from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# openId/views.py

def home(request):
    return HttpResponse("Welcome to the OpenID home page")
