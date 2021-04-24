>>> from django.forms import ModelForm
>>> from shoes.models import Shoe

# Create the form class.
>>> class ShoesForm(ModelForm):
...     class Meta:
...         model = Shoes
...         fields = ['Color', 'Size', 'Model', 'Style']