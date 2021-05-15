from django.shortcuts import render
from shoes.forms import ShoeForm, ShoeImageFormSet, ShoeImageInlineFormset, ShoeOrderForm
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from shoes.models import ShoeImage, Shoe, ShoeBrand
from django.shortcuts import get_object_or_404

# Create your views here.

from . import models

from django.views.generic import ListView, UpdateView, CreateView, DeleteView

class ShoeListView(LoginRequiredMixin, ListView):
    
    model = models.Shoe
    template_name = 'shoes/shoes_list.html'

    def get_queryset(self):
        qs = super().get_queryset()

        self.filter_form.is_valid()
        
        for field, value in self.filter_form.cleaned_data.items():
            if value:
                qs = qs.filter(**{field: value})
            
        return qs

    def dispatch(self, request, *args, **kwargs):
        self.filter_form = ShoeForm(request.GET)
        self.order_form = ShoeOrderForm(request.GET)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(form=self.filter_form, order_form=self.order_form, **kwargs)

    def get_ordering(self):
        
        if self.order_form.is_valid():
            return self.order_form.cleaned_data.get('order')
        else:
            return self.ordering 

class CartUpdateView(UpdateView):
    model = models.Shoe
    fields = ['cart']
    template_name_suffix = '_update_form'
    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({ 'cart': self.object.cart })

class UrgentView(UpdateView):
    model = models.Shoe
    fields = ['urgent']
    template_name_suffix = '_update_form'
    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({ 'urgent': self.object.urgent })

class minicartView(LoginRequiredMixin, ListView):
    
    model = models.Shoe
    template_name = 'shoes/minicartView_list.html'
    queryset = model.objects.filter(cart=True)

class FavouriteUpdateView(UpdateView):
    model = models.Shoe
    fields = ['favourite']
    template_name_suffix = '_update_form'
    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({ 'favourite': self.object.favourite })

class favouriteView(LoginRequiredMixin, ListView):
    
    model = models.Shoe
    template_name = 'shoes/favouriteView_list.html'
    queryset = model.objects.filter(favourite=True)
    
class ShoeDeleteView(LoginRequiredMixin, DeleteView):

    template_name = 'shoes/manage/delete_item.html'
    model = models.Shoe
    success_url = reverse_lazy('manage')
    
from django.contrib.auth.decorators import login_required

@login_required
def create_shoe(request):
    
    if request.method == 'POST':
        form = ShoeForm(request.POST)
        formset = ShoeImageFormSet(request.POST, request.FILES)
        
        if all( [ form.is_valid(), formset.is_valid() ]):
            shoe_instance = form.save()
            image_instance = formset.save(commit=False)
            for instance in image_instance:
                instance.shoe = shoe_instance
                instance.save()
                print(instance.shoe)
            return redirect('manage')

    else:
        form = ShoeForm()
        formset = ShoeImageFormSet(queryset=ShoeImage.objects.none())
    return render(request, "shoes/manage/shoe_form.html", {
        'form': form,
        'formset': formset,
    })

@login_required
def edit_shoe(request, pk):
    shoe = get_object_or_404(Shoe, pk=pk)
    if request.method == 'POST':
        form = ShoeForm(request.POST, instance=shoe)
        formset = ShoeImageInlineFormset(request.POST, request.FILES, instance=shoe)
        
        if all( [ form.is_valid(), formset.is_valid() ]):
            form.save()
            formset.save()
            return redirect('manage')

    else:
        form = ShoeForm(instance=shoe)
        formset = ShoeImageInlineFormset(instance=shoe)
    return render(request, "shoes/manage/shoe_form.html", {
        'form': form,
        'formset': formset,
    })

@login_required
def image_view(request, pk):
    shoe = get_object_or_404(Shoe, pk=pk)
    
    return render(request, 'shoes/imageView.html', {
        'shoeimages': shoe.shoeimage_set.all(),
    })


from django.core.mail import send_mail
from django.conf import settings

def order_list(request):

    if request.method == 'POST':
        queryset = models.Shoe.objects.filter(cart=True)
        ids = []
        for itm in queryset:
            
            ids.append(f" \n \n Style: {itm.style}; \n ID: {itm.pk}; \n Urgent: {itm.urgent}")

        queryset.update(cart=False, urgent=False)
        message = request.POST['message']
        for id in ids: message += str(id)
        send_mail('Order List',
         message, 
         settings.EMAIL_HOST_USER,
         settings.RECIPIENT_LIST, 
         fail_silently=False)
    return render(request, 'shoes/order_succeed.html')

class BrandCreate(CreateView):
    template_name = 'shoes/brand_form.html'
    model = ShoeBrand
    fields = ['brand']

class BrandUpdate(UpdateView):
    template_name = 'shoes/brand_form.html'
    model = ShoeBrand
    fields = ['brand']

class BrandDelete(DeleteView):
    template_name = 'shoes/brand_form.html'
    model = ShoeBrand
    success_url = reverse_lazy('manage')