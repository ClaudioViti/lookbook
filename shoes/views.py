from django.shortcuts import render
from shoes.forms import ShoeForm, ShoeImageFormSet, ShoeImageInlineFormset, ShoeOrderForm, BrandForm, CartAddForm, UrgentAddForm, ShoeCartsForm, ShoeFavouriteForm, modelformset_factory
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from shoes.models import ShoeImage, Shoe, ShoeBrand
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

from . import models

from django.views.generic import ListView, UpdateView, CreateView, DeleteView, FormView

class ShoeListView(LoginRequiredMixin, ListView):
    
    model = models.Shoe
    template_name = 'shoes/shoes_list.html'

    def get_queryset(self):
        qs = super().get_queryset()

        self.filter_form.is_valid()
        
        for field, value in self.filter_form.cleaned_data.items():
            if value:
                qs = qs.filter(**{field: value})
        if not self.request.user.is_staff:                                                  # multi user enable
            
            qs = qs.filter(user=self.request.user)                                       # multi user enable
        return qs

    def dispatch(self, request, *args, **kwargs):
        self.filter_form = ShoeForm(request.GET)
        self.order_form = ShoeOrderForm(request.GET)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
         
        # view - get_context_data() method
        context = super().get_context_data(form=self.filter_form, order_form=self.order_form, **kwargs)
        context['cart_ids'] = self.request.user.cart_items.values_list('pk', flat=True)
        context['favourite_ids'] = self.request.user.favourite_items.values_list('pk', flat=True)
        context['urgent_ids'] = self.request.user.favourite_items.values_list('pk', flat=True)
        return context
        

    def get_ordering(self):
        
        if self.order_form.is_valid():
            return self.order_form.cleaned_data.get('order')
        else:
            return self.ordering 
     

class CartUpdateView(UpdateView):
    model = models.Shoe
    form_class = CartAddForm
    template_name_suffix = '_update_form'
    def form_valid(self, form):
        to_cart = form.cleaned_data.get('cart', False)
        if to_cart:
             self.request.user.cart_items.add(self.object)
        else:
             self.request.user.cart_items.remove(self.object)
        print(self.request.user.cart_items.all())
        return JsonResponse({ 'cart': to_cart })

class UrgentUpdateView(UpdateView):
    print('ok')
    model = models.Shoe
    form_class = UrgentAddForm
    template_name_suffix = '_update_form'
    def form_valid(self, form):
        to_urgent = form.cleaned_data.get('urgent', False)
        print(to_urgent)
        if to_urgent:
             self.request.user.urgent_items.add(self.object)
        else:
             self.request.user.urgent_items.remove(self.object)
        print(self.request.user.urgent_items.all())
        return JsonResponse({ 'urgent': to_urgent })

class OrderedUpdateView(UpdateView):
    model = models.Shoe
    fields = ['ordered']
    template_name_suffix = '_update_form'
    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({ 'ordered': self.object.cart })


class minicartView(LoginRequiredMixin, ListView):
    
    model = models.Shoe
    template_name = 'shoes/minicartView_list.html'

    def get_queryset(self):                                                 # multi user enable
        if self.request.user.is_staff:
            print("staff see everything")
            queryset = Shoe.objects.filter(cart_user__in = User.objects.all()).distinct()                       
        else:
            print("user sees own")
        
            queryset = self.request.user.cart_items.all()
            
        return queryset
    def get_context_data(self, **kwargs):
         
        # view - get_context_data() method
        context = super().get_context_data(**kwargs)
        context['urgent_ids'] = self.request.user.urgent_items.values_list('pk', flat=True)
        context['cart_ids'] = self.request.user.cart_items.values_list('pk', flat=True)
        context['ordered_ids'] = self.request.user.ordered_items.values_list('pk', flat=True)
        context['delivered_ids'] = self.request.user.delivered_items.values_list('pk', flat=True)

        formset_class = modelformset_factory(Shoe, form=ShoeCartsForm, extra=0)
       
        context['shoe_formset'] = formset_class(queryset=context['object_list'])
        
        return context


class FavouriteUpdateView(UpdateView):
    model = models.Shoe
    fields = ['favourite']
    template_name_suffix = '_update_form'
    def form_valid(self, form):
        to_favourite = form.cleaned_data.get('favourite', False)
        if to_favourite:
             self.request.user.favourite_items.add(self.object)
        else:
             self.request.user.favourite_items.remove(self.object)
        
        return JsonResponse({ 'favourite': to_favourite })

class favouriteView(LoginRequiredMixin, ListView):
    
    model = models.Shoe
    template_name = 'shoes/favouriteView_list.html'
    queryset = model.objects.filter(favourite=True)
    def get_queryset(self):                                                 # multi user enable
        if self.request.user.is_staff:
            print("staff see everything")
            queryset = Shoe.objects.filter(cart_user__in = User.objects.all()).distinct()                                     
        else:
            print("user sees own")
        queryset = self.request.user.favourite_items.all()
        return queryset
    def get_context_data(self, **kwargs):
         
        # view - get_context_data() method
        context = super().get_context_data(**kwargs)
        context['favourite_ids'] = self.request.user.favourite_items.values_list('pk', flat=True)


        formset_class = modelformset_factory(Shoe, form=ShoeFavouriteForm, extra=0)
       
        context['shoe_formset'] = formset_class(queryset=context['object_list'])
        
        return context
    
    
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
     #   queryset = models.Shoe.objects.filter(cart=True)
       # if not request.user.is_staff:                                       # multi user enable
        queryset = request.user.cart_items.all()
        queryset = queryset.filter(user=request.user)                   # multi user enable
        
        ids = []
        for itm in queryset:
            
            ids.append(f" \n \n Style: {itm.style}; \n ID: {itm.pk}; \n User: {itm.user}; \n Urgent: {itm.urgent}")

        request.user.cart_items.clear()
        #queryset.update(cart=False, urgent=False)
        message = request.POST['message']
        for id in ids: message += str(id)
        send_mail('Order List',
         message, 
         settings.EMAIL_HOST_USER,
         settings.RECIPIENT_LIST, 
         fail_silently=False)
    return render(request, 'shoes/order_succeed.html')

class BrandCreate(LoginRequiredMixin, CreateView):
    template_name = 'shoes/manage/brand_manage.html'
    model = ShoeBrand
    fields = ['brand']
    def get_success_url(self):
        return reverse('manage')

class BrandUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'shoes/manage/brand_manage.html'
    model = ShoeBrand
    fields = ['brand']
    def get_success_url(self):
        return reverse('manage')

class BrandDelete(LoginRequiredMixin, DeleteView):
    template_name = 'shoes/manage/brand_manage.html'
    model = ShoeBrand
    success_url = reverse_lazy('manage')

class BrandManage(LoginRequiredMixin, FormView):

    template_name = 'shoes/manage/brand_form.html'
    form_class = BrandForm
    
    def form_valid(self, form):
        print(self.request.POST['name'])
        
        if self.request.POST['name'] == 'delete':
            return redirect('brand-delete', pk=form.cleaned_data['brand'].pk)
        elif self.request.POST['name'] == 'edit':
            return redirect('brand-update', pk=form.cleaned_data['brand'].pk)
        
