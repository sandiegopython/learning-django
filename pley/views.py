from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from restaurants.models import Restaurant
from restaurants.forms import ReviewForm


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
            'reviews': self.object.review_set.all(),
        })
        return super(RestaurantDetailView, self).get_context_data(**kwargs)

detail = RestaurantDetailView.as_view()


class CreateReviewView(TemplateView):

    """Page for creating a new restaurant review"""

    template_name = 'create_review.html'

    def get(self, request, pk):
        self.form = ReviewForm()
        return super(CreateReviewView, self).get(request, pk)

    def get_context_data(self, **kwargs):
        return {'form': self.form}

create_review = CreateReviewView.as_view()
