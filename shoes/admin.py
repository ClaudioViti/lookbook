from django.contrib import admin

# Register your models here.

from .models import Shoe, ShoeImages

admin.site.register(Shoe)
admin.site.register(ShoeImages)
