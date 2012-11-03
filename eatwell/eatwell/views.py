from django.http import HttpResponse


def home(request):
    """A simple page containing just "Hello world!\""""
    return HttpResponse("Hello world!")


def contact(request):
    """Page stating our contact information"""
    return HttpResponse("Contact information: 888.888.8888")
