from django.conf.urls import patterns, url
from rest_framework import generics
from restaurants import models

urlpatterns = patterns('restaurants.api_views',
    url('^restaurant/$', generics.ListAPIView().as_view(model=models.Restaurant)),
    url('^restaurant/(?P<pk>[\d]+)/$', generics.RetrieveUpdateAPIView().as_view(model=models.Restaurant)),
)
