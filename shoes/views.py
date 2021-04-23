from django.shortcuts import render

# Create your views here.

from . import models

from django.views.generic import ListView

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from shoes.models import Shoe

class ShoeListView(ListView):

    model = models.Shoe
    template_name = 'shoes/shoes_list.html'

    def get_queryset(self):
        qs = super().get_queryset()

        color = self.request.GET.get('color')
        if color:
            qs = qs.filter(color=color)
​
        return qs