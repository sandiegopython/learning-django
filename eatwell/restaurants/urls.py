from django.conf.urls import patterns, url

urlpatterns = patterns('restaurants.views',
     url(r'^$', 'restaurant_list', name='restaurants'),
     url(r'^(?P<pk>\d+)/$', 'detail',
         name='restaurant'),
     url(r'^(?P<pk>\d+)/review$', 'create_review',
         name='create_review'),
     )
