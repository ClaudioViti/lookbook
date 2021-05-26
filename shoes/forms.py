from django.forms import ModelForm
from shoes.models import Shoe, ShoeImage, ShoeBrand
from django import forms
from django.forms.models import modelformset_factory
from django.forms import inlineformset_factory

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

class UrgentForm(ModelForm):
    class Meta:
        model = Shoe
        fields = ['id']
    urgent = forms.BooleanField(required=False)