from django.db import models

# Create your models here.

class Shoe(models.Model):
    model_id = models.ForeignKey(ID, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=200)
    brand = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    heelHeight = models.IntegerField(default=0)
    imageURL = models.URL()