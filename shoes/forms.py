from django.forms import ModelForm
from shoes.models import Shoe
from django import forms

# Create the form class.
class ShoesForm(ModelForm):
     class Meta:
         model = Shoe
         fields = ['color', 'size', 'model', 'style', 'toe', 'slingback', 'platform', 'favourite']
