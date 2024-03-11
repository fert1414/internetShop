from django.contrib import admin

from goods import models

admin.site.register(models.Categories)
admin.site.register(models.Products)