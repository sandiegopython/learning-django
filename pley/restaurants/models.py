from django.db import models
from django.core import urlresolvers
from django.contrib.localflavor.us.models import USStateField


class Restaurant(models.Model):
    name = models.CharField(max_length=300)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = USStateField(max_length=2, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)

    def address(self):
        """Return full address of restaurant, formatted nicely"""
        if not self.city:
            return ""
        address = self.address1
        if self.address2:
            address += "\n" + self.address2
        return address + "\n{s.city}, {s.state} {s.zip_code}".format(s=self)

    def get_absolute_url(self):
        return urlresolvers.reverse('restaurant', args=[self.pk])

    def __unicode__(self):
        return self.name


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)

    def __unicode__(self):
        return self.title
