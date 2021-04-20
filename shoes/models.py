from django.db import models

# Create your models here.

class Shoe(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    model_id = models.CharField(max_length=10)
    model_name = models.CharField(max_length=200)
    brand = models.CharField()
    size = models.IntegerField(default=0)
    heel_height = models.IntegerField(default=0)
    image = models.ImageField()