from django.shortcuts import render

# Create your views here.

from . import models

from django.views.generic import ListView

FILTER_FIELDS = ['color', 'size', 'model', 'slingback', 'brand', 'heel_height']

class ShoeListView(ListView):

    model = models.Shoe
    template_name = 'shoes/shoes_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        for field in FILTER_FIELDS:
            value = self.request.GET.get(field)
            if value:
                qs = qs.filter(**{field: value})

        return qs