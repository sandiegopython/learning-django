from django.http import HttpResponse


def home(request):
    """A simple page containing just "Hello world!\""""
    return HttpResponse("Hello world!" '<a href="/contact">Contact us</a>')


def contact(request):
    """Page stating our contact information"""
    return HttpResponse("""
        <!DOCTYPE html>
        <html>
            <head>
                <title>Contact Us</title>
            </head>
            <body>
                <nav>
                    <a href="/">Home</a>
                </nav>
                <header><h2>Contact Us</h2></header>
                <p>
                <strong>Phone:</strong> 888.888.8888<br>
                <strong>Email:</strong> pley@example.com
                </p>
            </body>
        </html>
    """)
