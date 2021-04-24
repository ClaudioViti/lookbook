from django.forms import ModelForm
from shoes.models import Shoe

# Create the form class.
class ShoesForm(ModelForm):
     class Meta:
         model = Shoe
         fields = ['color', 'size', 'model', 'style']