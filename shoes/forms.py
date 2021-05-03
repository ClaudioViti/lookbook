from django.forms import ModelForm
from shoes.models import Shoe
from django.forms import BaseModelFormSet

# Create the form class.
class ShoesForm(ModelForm):
     class Meta:
         model = Shoe
         fields = ['color', 'size', 'model', 'style', 'toe', 'slingback', 'platform', 'favourite']






    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        