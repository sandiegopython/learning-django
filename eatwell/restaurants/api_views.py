from rest_framework import serializers

from restaurants import models

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ('id', 'name', 'address1', 'address2', 'city', 'state', 'zip_code')


