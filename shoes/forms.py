from django.forms import ModelForm
from shoes.models import Shoe

# Create the form class.
class ShoesForm(ModelForm):
     class Meta:
         model = Shoe
         fields = ['color', 'size', 'model', 'style', 'toe', 'slingback', 'platform', 'favourite']


from django.forms import BaseModelFormSet


class ImageFormSet(ImageFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Shoe.objects.filter(name__startswith='O')