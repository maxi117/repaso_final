from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista2(request):
    return HttpResponse("<h1>Vista 2 App2</h1>")