from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

def home (request) :
    return render (request, "App/home.html")

def about (request) :
    return render (request, "App/about.html")

def tienda  (request) :
    return render (request, "App/tienda.html")

def blog (request) :
    return render (request, "App/blog.html")

def contacto (request) :
    return render (request, "App/contacto.html")
