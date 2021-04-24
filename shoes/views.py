from django.shortcuts import render
from shoes.forms import ShoesForm

# Create your views here.

from . import models

from django.views.generic import ListView

FILTER_FIELDS = ['color', 'size', 'model', 'slingback', 'brand', 'heel_height']

class ShoeListView(ListView):

    model = models.Shoe
    template_name = 'shoes/shoes_list.html'

    def get_queryset(self):
        qs = super().get_queryset()

        self.form.is_valid()
        
        for field, value in self.form.cleaned_data.items():
            qs = qs.filter(**{field: value})
            
        return qs

    def dispatch(self, request, *args, **kwargs):
        self.form = ShoesForm(request.GET)
        return super().dispatch(request, *args, **kwargs)