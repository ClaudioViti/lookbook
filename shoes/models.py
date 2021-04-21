from django.db import models

# Create your models here.

class Shoe(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    style = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    size = models.FloatField(default=0)
    heel_height = models.IntegerField(default=0)
    heel_kind = models.CharField(max_length=20)
    plateau_heitht = models.IntegerField(default=0)
    season = models.CharField(max_length=10)
    year = models.FloatField(default=0)
    comfortable = models.IntegerField(default=0)
    def real_heel(self):
        return self.heel_height - self.plateau_heitht

    image = models.ImageField()