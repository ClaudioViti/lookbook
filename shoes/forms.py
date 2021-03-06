from django.forms import ModelForm
from shoes.models import Shoe, ShoeImage, ShoeBrand, AccountConfig
from django import forms
from django.forms.models import modelformset_factory
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Create the form class.
class SearchForm(ModelForm):
     class Meta:
         model = Shoe
         fields = ['color', 'size', 'model', 'style', 'toe', 'slingback', 'platform', 'favourite']

class ShoeAdminForm(ModelForm):
    class Meta:
         model = Shoe
         fields = '__all__'

class ShoeForm(ModelForm):
    class Meta:
         model = Shoe
         exclude = ['user', 'available', 'cart_user', 'favourite_user', 'urgent_user', 'ordered_user', 'delivered_user', 'terminated_user']

ShoeImageFormSet = modelformset_factory(ShoeImage, fields=('image',), extra=3)
ShoeImageInlineFormset = inlineformset_factory(Shoe, ShoeImage, fields=('image',))

class ShoeOrderForm(forms.Form):
    order = forms.ChoiceField(choices=(('', '---------'), ('pk', 'ID'), ('-year', 'Newer'),('year', 'Older'), ('-heel_height', 'High Heel'), ('heel_height', 'Low Heel'), ('comfort', 'Comfort'), ('ordered', 'Common')), required=False)

class ShoeBrandForm(ModelForm):
    class Meta:
         model = ShoeBrand
         fields = '__all__'

class BrandForm(forms.Form):
    brand = forms.ModelChoiceField(queryset = ShoeBrand.objects.all() )
    
class CartAddForm(ModelForm):
    class Meta:
        model = Shoe
        fields = ['id']
    cart = forms.BooleanField(required=False)

class FavouriteAddForm(ModelForm):
    class Meta:
        model = Shoe
        fields = ['id']
    favourite = forms.BooleanField(required=False)

class UrgentAddForm(ModelForm):
    class Meta:
        model = Shoe
        fields = ['id']
    urgent = forms.BooleanField(required=False)

from django.db.models import Exists, OuterRef

class ShoeCartsForm(ModelForm):
    class Meta:
        model = Shoe
        fields = ['cart_user', 'urgent_user', 'ordered_user', 'delivered_user', 'terminated_user', 'id']
        widgets = {'id': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cart_user'].queryset = self.fields['cart_user'].queryset.annotate(selected=Exists(self.instance.cart_user.filter(pk=OuterRef('pk')))).order_by('-selected')
        self.fields['urgent_user'].queryset = self.fields['urgent_user'].queryset.annotate(selected=Exists(self.instance.urgent_user.filter(pk=OuterRef('pk')))).order_by('-selected')
        self.fields['ordered_user'].queryset = self.fields['ordered_user'].queryset.annotate(selected=Exists(self.instance.ordered_user.filter(pk=OuterRef('pk')))).order_by('-selected')
        self.fields['delivered_user'].queryset = self.fields['delivered_user'].queryset.annotate(selected=Exists(self.instance.delivered_user.filter(pk=OuterRef('pk')))).order_by('-selected')

    def clean(self):
        cleaned_data = super().clean()
        delivered_users = cleaned_data.get("delivered_user")  # fill the field name
        ordered_users = cleaned_data.get("ordered_user")  # fill the field name
        cart_users = cleaned_data.get("cart_user")  # fill the field name
        urgent_users = cleaned_data.get("urgent_user")  # fill the field name
        
        errors = []
        valid_user_pks = []
        for user in delivered_users:
            if user not in ordered_users:
                errors.append(
                    ValidationError('User %(name)s is not in list of users who made order',
                                    params={'name': user.username}),
                ) 
            else:
                valid_user_pks.append(user.pk)  
        
        if errors:
       
            self.data = self.data.copy()
            self.fields['delivered_user'].value = User.objects.none()
    
           # self.fields['delivered_user'].queryset = User.objects.all()
            
        
        for user in urgent_users:
            if user not in cart_users:
                errors.append(
                    ValidationError('User %(name)s is not in list of users in the cart',
                                    params={'name': user.username}),
                ) 
        if errors:
            raise ValidationError(errors)

class ShoeFavouriteForm(ModelForm):
    class Meta:
        model = Shoe
        fields = ['favourite_user', 'id']
        widgets = {'id': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['favourite_user'].queryset = self.fields['favourite_user'].queryset.annotate(selected=Exists(self.instance.favourite_user.filter(pk=OuterRef('pk')))).order_by('-selected')

class ShoeOrdersForm(ModelForm):
    class Meta:
        model = Shoe
        fields = ['id']
        widgets = {'id': forms.HiddenInput()}
    terminated = forms.BooleanField(required=False)

class ShoeOrdersAdminForm(ModelForm):
    class Meta:
        model = Shoe
        fields = ['ordered_user', 'id', 'delivered_user', 'terminated_user']
        widgets = {'id': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ordered_user'].queryset = self.fields['ordered_user'].queryset.annotate(selected=Exists(self.instance.ordered_user.filter(pk=OuterRef('pk')))).order_by('-selected')
        self.fields['delivered_user'].queryset = self.fields['delivered_user'].queryset.annotate(selected=Exists(self.instance.delivered_user.filter(pk=OuterRef('pk')))).order_by('-selected')
        self.fields['terminated_user'].queryset = self.fields['terminated_user'].queryset.annotate(selected=Exists(self.instance.terminated_user.filter(pk=OuterRef('pk')))).order_by('-selected')
    terminated = forms.BooleanField(required=False)


class ConfForm(ModelForm):
    class Meta:
         model = AccountConfig
         fields = ['paginate', 'dark_mode' ]