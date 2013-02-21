from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'eatwell.views.home', name='home'),
     url(r'^contact$', 'eatwell.views.contact', name='contact'),
     url(r'^restaurants/', include('restaurants.urls')),
     url(r'^admin/', include(admin.site.urls)),
)
