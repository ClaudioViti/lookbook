from django.contrib import admin

# Register your models here.

from .models import Shoe, Shoe_second_image

admin.site.register(Shoe)
admin.site.register(Shoe_second_image)
