from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

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


class RestaurantDetailView(TemplateView):

    """Page displaying details for an individual restaurant"""

    template_name = 'restaurant_detail.html'

    def get(self, request, restaurant_id):
        self.restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        return super(RestaurantDetailView, self).get(request, restaurant_id)

    def get_context_data(self):
        return {
            'title': "Restaurant: {0}".format(self.restaurant.name),
            'restaurant': self.restaurant,
        }

detail = RestaurantDetailView.as_view()
