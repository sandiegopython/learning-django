from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """A simple page containing just "Hello world!\""""
    return HttpResponse("Hello world!" '<a href="/contact">Contact us</a>')


def contact(request):
    """Page stating our contact information"""
    return render(request, "contact.html")
