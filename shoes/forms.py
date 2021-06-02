from django.forms import ModelForm
from shoes.models import Shoe, ShoeImage, ShoeBrand
from django import forms
from django.forms.models import modelformset_factory
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError


# Create the form class.
class SearchForm(ModelForm):
     class Meta:
         model = Shoe
         fields = ['color', 'size', 'model', 'style', 'toe', 'slingback', 'platform', 'favourite']

class ShoeForm(ModelForm):
    class Meta:
         model = Shoe
         fields = '__all__'

ShoeImageFormSet = modelformset_factory(ShoeImage, fields=('image',), extra=3)
ShoeImageInlineFormset = inlineformset_factory(Shoe, ShoeImage, fields=('image',))

class ShoeOrderForm(forms.Form):
    order = forms.ChoiceField(choices=(('', '---------'), ('pk', 'ID'), ('-year', 'Newer'),('year', 'Older'), ('-heel_height', 'High Heel'), ('heel_height', 'Low Heel'), ('comfort', 'Comfort')), required=False)

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

class ShoeCartsForm(ModelForm):
    class Meta:
        model = Shoe
        fields = ['cart_user', 'urgent_user', 'ordered_user', 'delivered_user', 'id']
        widgets = {'id': forms.HiddenInput()}
    def clean(self):
        cleaned_data = super().clean()
        delivered_users = cleaned_data.get("delivered_user")  # fill the field name
        ordered_users = cleaned_data.get("ordered_user")  # fill the field name
        cart_users = cleaned_data.get("cart_user")  # fill the field name
        urgent_users = cleaned_data.get("urgent_user")  # fill the field name
        
        errors = []
        for user in delivered_users:
            if user not in ordered_users:
                errors.append(
                    ValidationError('User %(name)s is not in list of users who made order',
                                    params={'name': user.username}),
                ) 
        if errors:
       
            self.data = self.data.copy()
           # self.data['delivered_user'] = User.objects.none()
    
            self.fields['delivered_user'].queryset.none()
            raise ValidationError(errors)

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

