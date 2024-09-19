# from django.shortcuts import render

# Create your views here.
# openId/views.py

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the OpenID home page")
