from django.db import models

# Create your models here.

class Shoe(models.Model):
    SEAS_CHOICES = (
    ("AW", "Autumn Winter"),
    ("SS", "Spring Summer"),
    )
    MODEL_CHOICES = (
    ("Décolleté", "Décolleté"),
    ("Mules", "Mules"),
    ("Sabot", "Sabot"),
    ("Clogs", "Clogs"),
    ("Mocassins", "Mocassins"),
    ("Brogues", "Brogues"),
    ("Open Toe", "Open Toe"),
    ("Sandals", "Sandals"),
    ("Wedges", "Wedges"),
    ("Platform", "Platform"),
    ("Ankle Boots", "Ankle Boots"),
    ("Lace-up", "Lace-up"),
    ("Gladiators", "Gladiators"),
    ("Boots", "Boots"),
    ("Sneakers", "Sneakers"),
    ("Pumps", "Pumps"),
    ("T-Strap", "T-Strap"),
    ("Ankle-Stra", "Ankle-Strap"),
    ("Texas", "Texas"),
    )
    STYLE_CHOICES = (
    ("Casual", "Casual"),
    ("Sport", "Sport"),
    ("Tennis", "Tennis"),
    ("Elegant", "Elegant"),
    ("Cerimony", "Cerimony"),
    ("Wedding", "Wedding"),
    ("Sea", "Sea"),
    )
    SIZE_CHOICES = (
    ("30", "30"), ("30.5", "30.5"), ("31", "31"), ("31.5", "31.5"), ("32", "32"), ("32.5", "32.5"), ("33", "33"), ("33.5", "33.5"), ("34", "34"), ("34.5", "34.5"),
    ("35", "35"), ("35.5", "35.5"), ("36", "36"), ("36.5", "36.5"), ("37", "37"), ("37.5", "37.5"), ("38", "30"), ("38.5", "38.5"), ("39", "39"), ("39.5", "39.5"),
    ("40", "40"), ("40.5", "40.5"), ("41", "41"), ("41.5", "41.5"), ("42", "42"), ("42.5", "42.5"), ("43", "43"), ("43.5", "43.5"), ("44", "44"), ("44.5", "44.5"), ("45", "45"),
    )
    COLOR_CHOICES = (
    ("Black", "Black"),
    ("Grey", "Grey"),
    ("White", "White"),
    ("Brown", "Bwoen"),
    ("Red", "Red"),
    ("Gold", "Gold"),
    ("Yellow", "Yellow"),
    ("Pink", "Pink"),
    ("Green", "Green"),
    ("Orange", "Orange"),
    ("Fuxia", "Fuxia"),
    ("Blue", "Blue"),
    )
    HEEL_KIND_CHOICES = (
    ("Large", "Large"),
    ("Wedge", "Wedge"),
    ("Stiletto", "Stiletto"),
    ("Brown", "Bwoen"),
    )

    COMFORT_CHOICES = [(i, i) for i in range(1,6)]
    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    model = models.CharField(max_length=200, choices=MODEL_CHOICES, blank=True, null=True)
    peep_toe = models.BooleanField(default=False)
    slingback = models.BooleanField(default=False)
    style = models.CharField(max_length=200, choices=STYLE_CHOICES, blank=True, null=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=200, blank=True, null=True)
    size = models.CharField(max_length=5, choices=SIZE_CHOICES, blank=True, null=True)
    color = models.CharField(max_length=200, choices=COLOR_CHOICES, blank=True, null=True)
    heel_height = models.IntegerField(default=0, blank=True, null=True)
    heel_kind = models.CharField(max_length=20, choices= HEEL_KIND_CHOICES, blank=True, null=True)
    plateau_height = models.IntegerField(default=0, blank=True, null=True)
    material = models.CharField(max_length=200, blank=True, null=True)
    season = models.CharField(max_length=10, choices=SEAS_CHOICES, blank=True, null=True)
    year = models.IntegerField(default=0)
    comfort = models.IntegerField(choices=COMFORT_CHOICES, blank=True, null=True)
    state = models.CharField(max_length=200, default="New", blank=True, null=True)
    available = models.BooleanField(default=True)
    info = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    def real_heel(self):
        return self.heel_height - self.plateau_height

    image = models.ImageField()