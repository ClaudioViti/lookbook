from django.shortcuts import render
from shoes.forms import ShoeForm, ShoeImageFormSet, ShoeImageInlineFormset, ShoeOrderForm, BrandForm, CartAddForm, UrgentAddForm, ShoeCartsForm, ShoeFavouriteForm, modelformset_factory, ShoeAdminForm, ShoeOrdersForm, ShoeOrdersAdminForm
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from shoes.models import ShoeImage, Shoe, ShoeBrand
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db.models import F, Q

# Create your views here.

from . import models

from django.views.generic import ListView, UpdateView, CreateView, DeleteView, FormView

class ShoeListView(LoginRequiredMixin, ListView):
    
    model = models.Shoe
    template_name = 'shoes/shoes_list.html'
    paginate_by = 4

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
        if request.user.is_staff:
            self.filter_form = ShoeAdminForm(request.GET)
        else:
            self.filter_form = ShoeForm(request.GET)

        self.order_form = ShoeOrderForm(request.GET)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
         
        # view - get_context_data() method
        context = super().get_context_data(form=self.filter_form, order_form=self.order_form, **kwargs)
        context['cart_ids'] = self.request.user.cart_items.values_list('pk', flat=True)
        context['favourite_ids'] = self.request.user.favourite_items.values_list('pk', flat=True)
        context['urgent_ids'] = self.request.user.favourite_items.values_list('pk', flat=True)
        context['admin_mail'] = settings.DEFAULT_FROM_EMAIL
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
    model = Shoe
    template_name = 'shoes/minicartView_list.html'

    formset = None
    formset_class = modelformset_factory(Shoe, form=ShoeCartsForm, extra=0)  # if it doesn't work uncomment dispatch

    # def dispatch(self, request, *args, **kwargs):
    #    self.formset_class = modelformset_factory(Shoe, form=ShoeCartsForm, extra=0)
    #    return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object_list = self.get_queryset()
        self.formset = self.get_formset(data=request.POST)
        if self.formset.is_valid():
            return self.formset_valid(self.formset)
        else:
            return self.formset_invalid(self.formset)


    def get_formset(self, data=None):
        kwargs = {
            "queryset": self.object_list,
        }
        if data:
            kwargs["data"] = data
        return self.formset_class(**kwargs)

    def formset_valid(self, formset):
        print("formset is valid")
        formset.save()
        return redirect('minicart')

    def formset_invalid(self, formset, error_anchor=None):
        return self.render_to_response(
            self.get_context_data()
        )

    def get_queryset(self):
        if self.request.user.is_staff:
            # print("staff see everything")
            queryset = Shoe.objects.filter(cart_user__in = User.objects.all()).distinct()                       
        else:
            # print("user sees own")
            queryset = self.request.user.cart_items.all()

        return queryset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['urgent_ids'] = self.request.user.urgent_items.values_list('pk', flat=True)
        context['cart_ids'] = self.request.user.cart_items.values_list('pk', flat=True)
        context['ordered_ids'] = self.request.user.ordered_items.values_list('pk', flat=True)
        context['delivered_ids'] = self.request.user.delivered_items.values_list('pk', flat=True)
        context['terminated_ids'] = self.request.user.terminated_items.values_list('pk', flat=True)

        if self.formset:
             context['shoe_formset'] = self.formset
        else:
            context['shoe_formset'] = self.formset_class(queryset=context['object_list'])

        return context

class favouriteView(LoginRequiredMixin, ListView):
    model = Shoe
    template_name = 'shoes/favouriteView_list.html'

    formset = None
    formset_class = modelformset_factory(Shoe, form=ShoeFavouriteForm, extra=0)  # if it doesn't work uncomment dispatch

    # def dispatch(self, request, *args, **kwargs):
    #    self.formset_class = modelformset_factory(Shoe, form=ShoeFavouritesForm, extra=0)
    #    return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object_list = self.get_queryset()
        self.formset = self.get_formset(data=request.POST)
        if self.formset.is_valid():
            return self.formset_valid(self.formset)
        else:
            return self.formset_invalid(self.formset)


    def get_formset(self, data=None):
        kwargs = {
            "queryset": self.object_list,
        }
        if data:
            kwargs["data"] = data
        return self.formset_class(**kwargs)

    def formset_valid(self, formset):
        print("formset is valid")
        formset.save()
        return redirect('favourites')

    def formset_invalid(self, formset, error_anchor=None):
        return self.render_to_response(
            self.get_context_data()
        )

    def get_queryset(self):
        if self.request.user.is_staff:
            # print("staff see everything")
            queryset = Shoe.objects.filter(favourite_user__in = User.objects.all()).distinct()                       
        else:
            # print("user sees own")
            queryset = self.request.user.favourite_items.all()

        return queryset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['favourite_ids'] = self.request.user.urgent_items.values_list('pk', flat=True)
  
        if self.formset:
             context['shoe_formset'] = self.formset
        else:
            context['shoe_formset'] = self.formset_class(queryset=context['object_list'])

        return context


class ordersView(LoginRequiredMixin, ListView):
    model = Shoe
    template_name = 'shoes/ordersView_list.html'

    formset = None


    # def dispatch(self, request, *args, **kwargs):
    #    self.formset_class = modelformset_factory(Shoe, form=ShoeFavouritesForm, extra=0)
    #    return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object_list = self.get_queryset()
        self.formset = self.get_formset(data=request.POST)
        if self.formset.is_valid():
            return self.formset_valid(self.formset)
        else:
            return self.formset_invalid(self.formset)


    def get_formset(self, data=None):
        if self.request.user.is_staff:
            formset_class = modelformset_factory(Shoe, form=ShoeOrdersAdminForm, extra=0)  # if it doesn't work uncomment dispatch
        else:
            formset_class = modelformset_factory(Shoe, form=ShoeOrdersForm, extra=0)
        kwargs = {
            "queryset": self.object_list,
        }
        if data:
            kwargs["data"] = data
        return formset_class(**kwargs)
    
    
    def formset_valid(self, formset):
        
        for form in formset:
            print(self.request)
            term = form.cleaned_data.get('terminated', False)
            
            obj = form.save()
            
            if term:
               
                
                self.request.user.terminated_items.add(obj)

                
        if not self.request.user.is_staff:
            return terminate_order(self.request)
        else:    
            return redirect('minicart')
    
    def formset_invalid(self, formset, error_anchor=None):
        print(formset.errors)
        print(self.request.POST)
        return self.render_to_response(
            self.get_context_data()
        )
    
    def get_queryset(self):
        if self.request.user.is_staff:
            # print("staff see everything")
            a = Q(ordered_user__isnull=False) 
            b = Q(delivered_user__isnull=False)
            c = Q(terminated_user__isnull=False)
            queryset = Shoe.objects.filter(a | b | c).distinct()
            
        else:
            # print("user sees own")
            a = Q(ordered_user=self.request.user) 
            b = Q(delivered_user=self.request.user)
            c = Q(terminated_user=self.request.user)
            queryset = Shoe.objects.filter(a | b | c).distinct()
            

        return queryset

    def get_context_data(self, **kwargs):
        if self.request.user.is_staff:
            formset_class = modelformset_factory(Shoe, form=ShoeOrdersAdminForm, extra=0)  # if it doesn't work uncomment dispatch
        else:
            formset_class = modelformset_factory(Shoe, form=ShoeOrdersForm, extra=0)

        context = super().get_context_data(**kwargs)
        context['terminated_items'] = self.request.user.urgent_items.values_list('pk', flat=True)
  
        if self.formset:
             context['shoe_formset'] = self.formset
        else:
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

    
class ShoeDeleteView(LoginRequiredMixin, DeleteView):

    template_name = 'shoes/manage/delete_item.html'
    model = models.Shoe
    success_url = reverse_lazy('manage')
    
from django.contrib.auth.decorators import login_required
from django.db.models import Count
@login_required
def create_shoe(request):
    
    if request.method == 'POST':
        if request.user.is_staff:
            form = ShoeAdminForm(request.POST)
        else:
            form = ShoeForm(request.POST)
        formset = ShoeImageFormSet(request.POST, request.FILES)
        
        if all( [ form.is_valid(), formset.is_valid() ]):
            
            shoe_instance = form.save()
            shoe_instance.user.add(request.user)
            image_instance = formset.save(commit=False)
            for instance in image_instance:
                instance.shoe = shoe_instance
                instance.save()
                print(instance.shoe)
            return redirect('manage')

    else:
        if request.user.is_staff:
            form = ShoeAdminForm()
        else:
            form = ShoeForm()
    
        formset = ShoeImageFormSet(queryset=ShoeImage.objects.none())
    return render(request, "shoes/manage/shoe_form.html", {
        'form': form,
        'formset': formset,
    })

@login_required
def edit_shoe(request, pk):
    queryset = Shoe.objects.all()
    if not request.user.is_superuser:
        queryset = queryset.annotate(user_count=Count('user')).filter(user_count=1)

    shoe = get_object_or_404(queryset, pk=pk)

    if request.method == 'POST':
        if request.user.is_staff:
            form = ShoeAdminForm(request.POST, instance=shoe)
        else:
            form = ShoeForm(request.POST, instance=shoe)
        
        formset = ShoeImageInlineFormset(request.POST, request.FILES, instance=shoe)
        
        if all( [ form.is_valid(), formset.is_valid() ]):
            form.save()
            formset.save()
            return redirect('manage')

    else:
        if request.user.is_staff:
            form = ShoeAdminForm(instance=shoe)
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
from django.contrib import messages


def order_list(request):

    if request.method == 'POST':
     #   queryset = models.Shoe.objects.filter(cart=True)
       # if not request.user.is_staff:                                       # multi user enable
        queryset = request.user.cart_items.all()
        
        
        ids = []
        itm_remove = []
        itm_not_ordered = []
        for itm in queryset:
            if not itm.ordered_user.exists() and itm.available == True:
                ids.append(f" \n \n Style: {itm.style}; \n ID: {itm.pk}; \n User: {request.user.username}; \n Urgent: {itm.urgent}")
                itm.ordered = F('ordered') + 1
                itm.save()
                itm_remove.append(itm)
                request.user.ordered_items.add(* request.user.cart_items.all())    
            else:
                itm_not_ordered.append(itm.pk)
            
            
                       
        request.user.cart_items.remove(*itm_remove)
        messages.add_message(request, messages.INFO, itm_not_ordered)
        
        print(itm.ordered)
        #queryset.update(cart=False, urgent=False)
        message = request.POST['message']
        for id in ids: message += str(id)
        if len(itm_remove):
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
        


class ShoeListManage(LoginRequiredMixin, ListView):
    
    model = models.Shoe
    template_name = 'shoes/shoe_list_manage.html'

    def get_queryset(self):
        qs = super().get_queryset()

        self.filter_form.is_valid()
        
        for field, value in self.filter_form.cleaned_data.items():
            if value:
                qs = qs.filter(**{field: value})
        if not self.request.user.is_staff:                                                  # multi user enable
              
            qs = qs.annotate(user_count=Count('user')).filter(user_count=1)                                 # multi user enable
            qs = qs.filter(user=self.request.user)
        return qs

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            self.filter_form = ShoeAdminForm(request.GET)
        else:
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
     

def terminate_order(request):

    if request.method == 'POST':
        queryset = request.user.terminated_items.all()
        
        ids = []
        itm_terminate = []
        print(len(queryset))
        for itm in queryset:
            if itm.terminated_user.exists():
                ids.append(f" \n \n ID: {itm.pk}; \n User: {request.user.username}; \n Urgent: {itm.urgent}")
                itm.ordered = F('ordered') + 1
                itm.save()
                itm_terminate.append(itm)
                

       

        message = request.POST['message']
        for id in ids: message += str(id)
        if len(itm_terminate):
            send_mail('Terminate Order List',
            message, 
            settings.EMAIL_HOST_USER,
            settings.RECIPIENT_LIST, 
            fail_silently=False)
    return render(request, 'shoes/terminate_succeed.html')




class TerminatedUpdateView(UpdateView):
    model = models.Shoe
    fields = ['terminated_user']
    
    
    def form_valid(self, form):
        to_terminated = form.cleaned_data.get('terminated', False)
        if to_terminated:
             self.request.user.terminated_items.add(self.object)
        else:
             self.request.user.terminated_items.remove(self.object)
        print(self.request.user.terminated_items.all())
        return JsonResponse({ 'terminated': to_terminated })



def terminateOrder(request, pk):
    shoe = get_object_or_404(Shoe, pk=pk)
        
   
    request.user.terminated_items.add(pk)
    return render(request, 'shoes/imageView.html', {'terminated_user': shoe.terminated_user.all()})
from django.contrib.auth.views import LoginView

class LoginViewCustom(LoginView):
    
    extra_context = {'admin_mail': settings.DEFAULT_FROM_EMAIL}
