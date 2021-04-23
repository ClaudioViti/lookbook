from django.shortcuts import render

# Create your views here.

from . import models

from django.views.generic import ListView

class ShoeListView(ListView):

    model = models.Shoe

def get_queryset(self):
return YourModel.objects.filter(age__lte=30)


from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from books.models import Shoe, Color

class ColorView(ListView):

    template_name = 'shoes/shoes_by_color.html'

    def get_queryset(self):
        self.shoes = get_object_or_404(Shoes, name=self.kwargs['Black'])
        return Shoes.objects.filter(shoes=self.shoes)