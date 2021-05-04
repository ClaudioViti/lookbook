from django.forms import ModelForm
from shoes.models import Shoe, ShoeImage
from django import forms
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

ShoeImageFormSet = inlineformset_factory(Shoe, ShoeImage, fields=('image',))