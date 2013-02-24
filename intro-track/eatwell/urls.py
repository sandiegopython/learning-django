from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'restaurants.views.home', name='home'),
    url(r'^contact/$', 'restaurants.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^restaurants/$', 'restaurants.views.restaurant_list', name='restaurant_list'),
    url(r'^restaurants/(?P<pk>\d+)/$', 'restaurants.views.restaurant_detail', name='restaurant_detail'),
    url(r'^restaurants/(?P<pk>\d+)/review/$', 'restaurants.views.write_review', name='restaurant_review'),
)