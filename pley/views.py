from django.http import HttpResponse


def home(request):
    """A simple page containing just "Hello world!\""""
    return HttpResponse("Hello world!")
