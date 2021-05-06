from django.contrib import admin

# Register your models here.

from .models import Shoe, ShoeImage, ShoeBrand

admin.site.register(Shoe)
admin.site.register(ShoeImage)
admin.site.register(ShoeBrand)
