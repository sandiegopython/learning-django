from django.shortcuts import render


def home(request):
    """Pley homepage"""
    return render(request, "home.html", {'title': "Home"})


def contact(request):
    """Page stating our contact information"""
    return render(request, "contact.html", {'title': "Contact Us"})
