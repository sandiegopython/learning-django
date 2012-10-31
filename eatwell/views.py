from django.shortcuts import render


def home(request):
    """A simple page containing just "Hello world!\""""
    return render(request, "home.html")


def contact(request):
    """Page stating our contact information"""
    return render(request, "contact.html")
