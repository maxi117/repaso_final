from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista(request):
    return HttpResponse("<h1>Vista 1 App 1</h1>")