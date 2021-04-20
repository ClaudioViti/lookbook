from django.db import models

# Create your models here.

class Shoe(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    model_name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    size = models.FloatField(default=0)
    heel_height = models.IntegerField(default=0)
    image = models.ImageField()