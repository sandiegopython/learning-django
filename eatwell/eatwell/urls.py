from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'eatwell.views.home', name='home'),
     url(r'^api/restaurants/', include('restaurants.api_urls')),
     url(r'^contact$', 'eatwell.views.contact', name='contact'),
     url(r'^restaurants/', include('restaurants.urls')),
     url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
