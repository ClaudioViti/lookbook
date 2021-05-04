from django.forms import ModelForm
from shoes.models import Shoe, ShoeImage
from django import forms

# Create the form class.
class SearchForm(ModelForm):
     class Meta:
         model = Shoe
         fields = ['color', 'size', 'model', 'style', 'toe', 'slingback', 'platform', 'favourite']

class Shoe(ModelForm):
    class Meta:
         model = ShoeImage
         fields = '__all__'