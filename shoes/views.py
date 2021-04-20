from django.shortcuts import render

# Create your views here.

from . import models

from django.views.generic import ListView

class ShoeListView(ListView):

    model = models.Shoe