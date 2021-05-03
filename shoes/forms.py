from django.forms import ModelForm
from shoes.models import Shoe
from django import forms

# Create the form class.
class SearchForm(ModelForm):
     class Meta:
         model = Shoe
         fields = ['color', 'size', 'model', 'style', 'toe', 'slingback', 'platform', 'favourite']

class ShoeForm(ModelForm):
    class Meta:
         model = ShoeImage
         field = ['image']