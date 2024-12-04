from django.contrib import admin

# Register your models here.

from .models import Shoe, ShoeImage, ShoeBrand, AccountConfig

admin.site.register(Shoe)
admin.site.register(ShoeImage)
admin.site.register(ShoeBrand)
admin.site.register(AccountConfig)