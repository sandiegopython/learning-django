from django.contrib import admin

from restaurants import models


admin.site.register(models.Restaurant)
admin.site.register(models.Review)
