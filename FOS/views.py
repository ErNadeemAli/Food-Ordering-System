from django.shortcuts import render, HttpResponse

# Create your views here.

def mes(request):
    return HttpResponse('<h1>Food Ordering System</h1>')