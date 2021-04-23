from django.shortcuts import render

# Create your views here.

from . import models

from django.views.generic import ListView

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from shoes.models import Shoe, Color

class ShoeListView(ListView):

    model = models.Shoe

class ColorView(ListView):

    template_name = 'shoes/shoes_list.html'

    def get_queryset(self):
        self.shoes = get_object_or_404(Shoes, name=self.kwargs['Black'])
        return Shoes.objects.filter(shoes=self.shoes)