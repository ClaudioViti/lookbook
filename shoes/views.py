from django.shortcuts import render, redirect
from shoes.forms import ShoesForm
from django.http import JsonResponse
from django.conf import settings

# Create your views here.

from . import models

from django.views.generic import ListView, UpdateView

class ShoeListView(ListView):

    model = models.Shoe
    template_name = 'shoes/shoes_list.html'

    def get_queryset(self):
        qs = super().get_queryset()

        self.form.is_valid()
        
        for field, value in self.form.cleaned_data.items():
            if value:
                qs = qs.filter(**{field: value})
            
        return qs

    def dispatch(self, request, *args, **kwargs):
        self.form = ShoesForm(request.GET)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        if not request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        return super().get_context_data(form=self.form, **kwargs)

class FavouriteUpdateView(UpdateView):
    model = models.Shoe
    fields = ['favourite']
    template_name_suffix = '_update_form'
    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({ 'favourite': self.object.favourite })