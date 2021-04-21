from django.db import models

# Create your models here.

class Shoe(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    model = models.CharField(max_length=200, blank=True, null=True)
    style = models.CharField(max_length=200, blank=True, null=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    size = models.FloatField(default=0)
    color = models.CharField(max_length=200, blank=True, null=True)
    heel_height = models.FloatField(default=0, blank=True, null=True)
    heel_kind = models.CharField(max_length=20, blank=True, null=True)
    plateau_height = models.FloatField(default=0, blank=True, null=True)
    material = models.CharField(max_length=200, blank=True, null=True)
    season = models.CharField(max_length=10, blank=True, null=True)
    year = models.IntegerField(default=0)
    comfort = models.IntegerField(default=None, blank=True, null=True)
    state = models.CharField(max_length=200, default="New", blank=True, null=True)
    available = models.BooleanField(default=True)
    def real_heel(self):
        return self.heel_height - self.plateau_height

    image = models.ImageField()