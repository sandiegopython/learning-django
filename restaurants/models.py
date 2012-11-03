from django.db import models
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

    def __unicode__(self):
        return self.name
