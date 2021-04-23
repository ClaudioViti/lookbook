from django.shortcuts import render

# Create your views here.

from . import models

from django.views.generic import ListView

class ShoeListView(ListView):

    model = models.Shoe
    template_name = 'shoes/shoes_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        x = self.request.GET.get(field)
        if x:
            qs = qs.filter(color=x)
            qs = qs.filter(model=x)
        return qs