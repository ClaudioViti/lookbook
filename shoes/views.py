from django.shortcuts import render
from shoes.forms import ShoeForm, ShoeImageFormSet
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.

from . import models

from django.views.generic import ListView, UpdateView, CreateView, DeleteView

class ShoeListView(LoginRequiredMixin, ListView):
    
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
        self.form = ShoeForm(request.GET)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(form=self.form, **kwargs)

class FavouriteUpdateView(UpdateView):
    model = models.Shoe
    fields = ['favourite']
    template_name_suffix = '_update_form'
    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({ 'favourite': self.object.favourite })

class minicartView(LoginRequiredMixin, ListView):
    
    model = models.Shoe
    template_name = 'shoes/minicartView_list.html'
    queryset = model.objects.filter(favourite=True)


class ShoeManageView(LoginRequiredMixin, ListView):



    model = models.Shoe
        


class ShoeUpdateView(LoginRequiredMixin, UpdateView):
    
    fields = '__all__'
    template_name = 'shoes/manage/shoe_form.html'
    model = models.Shoe
    success_url = reverse_lazy('manage')

class ShoeDeleteView(LoginRequiredMixin, DeleteView):

    template_name = 'shoes/manage/delete_item.html'
    model = models.Shoe
    
def create_shoe(request):
    
    if request.method == 'POST':
        form = ShoeForm(request.POST)
        formset = ShoeImageFormSet(request.FILES)
        
         if all(form.is_valid(), formset.is_valid()):
            shoe = form.save()
            shoe = formset.save()
            return redirect('manage')

    else:
        form = ShoeForm()
        formset = ShoeImageFormSet()
    return render(request, "shoes/manage/shoe_form.html", {
        'form': form,
        'formset': formset,
    })