from django.views.generic import TemplateView

from restaurants.models import Restaurant


class Home(TemplateView):

    """Pley homepage"""

    template_name = 'home.html'

    def get_context_data(self):
        return {'title': "Home"}

home = Home.as_view()


class Contact(TemplateView):

    """Page stating our contact information"""

    template_name = 'contact.html'

    def get_context_data(self):
        return {'title': "Contact Us"}

contact = Contact.as_view()


class RestaurantListView(TemplateView):

    """Page to list all restaurants"""

    template_name = 'restaurant_list.html'

    def get_context_data(self):
        return {
            'title': "Restaurants",
            'restaurants': Restaurant.objects.all(),
        }

restaurant_list = RestaurantListView.as_view()
