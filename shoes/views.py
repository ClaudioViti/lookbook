from django.shortcuts import render

# Create your views here.

from . import models

from django.views.generic import ListView

class ShoeListView(ListView):

    model = models.Shoe
    template_name = 'shoes/shoes_list.html'

FILTER_FIELDS = ['color', 'size', 'model']
​
​
    def get_queryset(self):
        qs = super().get_queryset()
​
        for field in FILTER_FIELDS:
            value = self.request.GET.get(field)
            if value:
                qs = qs.filter(**{field: value})
​
        return qs