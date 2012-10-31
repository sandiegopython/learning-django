from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'eatwell.views.home', name='home'),
     url(r'^contact$', 'eatwell.views.contact', name='contact'),
     url(r'^restaurants/$', 'eatwell.views.restaurant_list', name='restaurants'),
     url(r'^restaurants/(?P<restaurant_id>\d+)/$', 'eatwell.views.detail',
         name='restaurant'),
    # url(r'^eatwell/', include('eatwell.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
