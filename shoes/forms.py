from django import forms

class Shoes(forms.Form):
    color = forms.CharField(max_length=100)
    size = forms.CharField(max_length=100)
