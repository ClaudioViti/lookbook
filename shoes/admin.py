from django.contrib import admin

# Register your models here.

from .models import Shoe, ShoeImage

admin.site.register(Shoe)
admin.site.register(ShoeImage)
