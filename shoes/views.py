from django.shortcuts import render
from shoes.forms import ShoesForm, ImageForm
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from shoes.models import ShoeImages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
        self.form = ShoesForm(request.GET)
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


    template_name = 'shoes/manage/manage_items.html'
    model = models.Shoe
    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':
    
        ImageForm = ImageForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
    
    
        if ImageForm.is_valid() and formset.is_valid():
            image_form = imageForm.save(commit=False)
            image_form.user = request.user
            image_form.save()
    
            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(image=Image_form, image=image)
                    photo.save()
            # use django messages framework
            messages.success(request, "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(postForm.errors, formset.errors)
    else:
        ImageForm = ImageForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'index.html',
                  {'ImageForm': ImageForm, 'formset': formset})

        
class ShoeCreateView(LoginRequiredMixin, CreateView):

    fields = '__all__'
    template_name = 'shoes/manage/shoe_form.html'
    model = models.Shoe
    

class ShoeUpdateView(LoginRequiredMixin, UpdateView):
    
    fields = '__all__'
    template_name = 'shoes/manage/shoe_form.html'
    model = models.Shoe
    success_url = reverse_lazy('manage')

class ShoeDeleteView(LoginRequiredMixin, DeleteView):

    template_name = 'shoes/manage/delete_item.html'
    model = models.Shoe
    


