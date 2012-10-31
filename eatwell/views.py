from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

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


class RestaurantListView(ListView):

    """Page to list all restaurants"""

    template_name = 'restaurant_list.html'
    model = Restaurant
    context_object_name = 'restaurants'

    def get_context_data(self, **kwargs):
        kwargs['title'] = "Restaurants"
        return super(RestaurantListView, self).get_context_data(**kwargs)

restaurant_list = RestaurantListView.as_view()


class RestaurantDetailView(DetailView):

    """Page displaying details for an individual restaurant"""

    template_name = 'restaurant_detail.html'
    model = Restaurant

    def get_context_data(self, **kwargs):
        kwargs.update({
            'title': "Restaurant: {0}".format(self.object.name),
        })
        return super(RestaurantDetailView, self).get_context_data(**kwargs)

detail = RestaurantDetailView.as_view()
