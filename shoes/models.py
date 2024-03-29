from django.db import models

# Create your models here.

class Shoe(models.Model):
    SEAS_CHOICES = (
    ("Autumn", "Autumn"),
    ("Winter", "Winter"),
    ("Spring", "Spring"),
    ("Summer", "Summer"),
    )
    MODEL_CHOICES = (
    ("Décolleté", "Décolleté"),
    ("D'Orsay", "D'Orsay"),
    ("V-neck", "V-neck"),
    ("Mules", "Mules"),
    ("Sabot", "Sabot"),
    ("Clogs", "Clogs"),
    ("Mocassins", "Mocassins"),
    ("Brogues", "Brogues"),
    ("Sandals", "Sandals"),
    ("Lace-up", "Lace-up"),
    ("Gladiators", "Gladiators"),
    ("Boots", "Boots"),
    ("Boots Texan", "Boots Texan"),
    ("Ankle Boots", "Ankle Boots"),
    ("Sock Boots", "Sock Boots"),
    ("Cuissardes", "Cuissardes"),
    ("Sneakers", "Sneakers"),
    ("Pumps", "Pumps"),
    ("T-Strap", "T-Strap"),
    ("Cross-Strap", "Cross-Strap"),
    ("Diagonal-Strap", "Diagonal-Strap"),
    ("Ankle-Strap", "Ankle-Strap"),
    ("Beatles", "Beatles"),
    ("Bikers", "Bikers"),
    ("Mary Jane", "Mary Jane"),
    ("Ballet Flats", "Ballets Flats"),
    ("Ballroom Dance Shoes", "Ballroom Dance Shoes"),
    ("Espadrille", "Espadrille"),
    ("Fantasy", "Fantasy"),
    ("Corset", "Corset"),
    ("Cut Out", "Cut Out"),
    ("Flip-flops", "Flip-flops"),
    )
    STYLE_CHOICES = (
    ("Casual", "Casual"),
    ("Sport", "Sport"),
    ("Tennis", "Tennis"),
    ("Elegant", "Elegant"),
    ("Cerimony", "Cerimony"),
    ("Wedding", "Wedding"),
    ("Office", "Office"),
    ("Evening", "Evening"),
    ("Sea", "Sea"),
    ("Home", "Home"),
    )
    SIZE_CHOICES = (
    ("30", "30"), ("30.5", "30.5"), ("31", "31"), ("31.5", "31.5"), ("32", "32"), ("32.5", "32.5"), ("33", "33"), ("33.5", "33.5"), ("34", "34"), ("34.5", "34.5"),
    ("35", "35"), ("35.5", "35.5"), ("36", "36"), ("36.5", "36.5"), ("37", "37"), ("37.5", "37.5"), ("38", "38"), ("38.5", "38.5"), ("39", "39"), ("39.5", "39.5"),
    ("40", "40"), ("40.5", "40.5"), ("41", "41"), ("41.5", "41.5"), ("42", "42"), ("42.5", "42.5"), ("43", "43"), ("43.5", "43.5"), ("44", "44"), ("44.5", "44.5"), ("45", "45"),
    )
    COLOR_CHOICES = (
    ("Black", "Black"),
    ("Nude", "Nude"),
    ("Gray", "Gray"),
    ("White", "White"),
    ("Brown", "Brown"),
    ("Beige", "Beige"),
    ("Red", "Red"),
    ("Gold", "Gold"),
    ("Yellow", "Yellow"),
    ("Pink", "Pink"),
    ("Green", "Green"),
    ("Orange", "Orange"),
    ("Fuchsia", "Fuchsia"),
    ("Blue", "Blue"),
    ("Azure", "Azure"),
    ("Silver", "Silver"),
    ("Purple", "Purple"),
    ("Wheat", "Wheat"),
    ("Glitter", "Glitter"),
    )
    HEEL_KIND_CHOICES = (
    ("Large", "Large"),
    ("Wedge", "Wedge"),
    ("Stiletto", "Stiletto"),
    ("Cone", "Cone"),
    ("Blade", "Blade"),
    ("Kitten", "Kitten"),
    ("Spool", "Spool"),
    ("Triangle", "Triangle"),
    )
    STATE_CHOICES = (
    ("New", "New"),
    ("Good conditions", "Good conditions"),
    ("To be cleaned", "To be cleaned"),
    ("Need service", "Need service"),
    )
    MATERIAL_CHOICES = (
    ("Leather", "Leather"),
    ("Patent leather", "Patent leather"),
    ("Suede leather", "Suede leather"),
    ("Rubber", "Rubber"),
    ("Fabric", "Fabric"),
    ("Wood", "Wood"),
    ("Cork", "Cork"),
    ("Synthetics", "Synthetics"),
    ("Microfiber", "Microfiber"),
    ("Plastic", "Plastic"),
    ("Vinyl", "Vinyl"),
    ("Polyethylene", "Polyethylene"),
    ("Other", "Other"),
    )
    TOE_CHOICES = (
    ("Peep", "Peep"),
    ("Open", "Open"),
    ("Rounded", "Rounded"),
    ("Pointed", "Pointed"),
    ("Square", "Square"),
    ("Almond", "Almond"),
    )
    COMFORT_CHOICES = [(i, i) for i in range(1,6)]
    
    PLANT_FIT_CHOICES = (
    ("Narrow", "Narrow"),
    ("Normal", "Normal"),
    ("Wide", "Wide"),
    )
    
    user = models.ManyToManyField('auth.User', related_name='user_items', blank=True)
    cart_user = models.ManyToManyField('auth.User', related_name='cart_items', blank=True)
    favourite_user = models.ManyToManyField('auth.User', related_name='favourite_items', blank=True)
    urgent_user = models.ManyToManyField('auth.User', related_name='urgent_items', blank=True)
    ordered_user = models.ManyToManyField('auth.User', related_name='ordered_items', blank=True)
    delivered_user = models.ManyToManyField('auth.User', related_name='delivered_items', blank=True)
    terminated_user = models.ManyToManyField('auth.User', related_name='terminated_items', blank=True)
    model = models.CharField(max_length=200, choices=MODEL_CHOICES, blank=True, null=True)
    platform = models.BooleanField(default=False)
    slingback = models.BooleanField(default=False)
    toe = models.CharField(max_length=20, choices=TOE_CHOICES, blank=True, null=True)
    style = models.CharField(max_length=200, choices=STYLE_CHOICES, blank=True, null=True)
    brand = models.ForeignKey('ShoeBrand', on_delete=models.SET_NULL, blank=True, null=True)
    SKU = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    size = models.CharField(max_length=5, choices=SIZE_CHOICES, blank=True, null=True)
    color = models.CharField(max_length=200, choices=COLOR_CHOICES, blank=True, null=True)
    sole_color = models.CharField(max_length=200, choices=COLOR_CHOICES, blank=True, null=True)
    heel_height = models.IntegerField(default=0, blank=True, null=True)
    heel_kind = models.CharField(max_length=20, choices= HEEL_KIND_CHOICES, blank=True, null=True)
    plateau_height = models.IntegerField(default=0, blank=True, null=True)
    sole_material = models.CharField(max_length=30, choices=MATERIAL_CHOICES, blank=True, null=True)
    lining_material = models.CharField(max_length=30, choices=MATERIAL_CHOICES, blank=True, null=True)
    upper_material = models.CharField(max_length=30, choices=MATERIAL_CHOICES, blank=True, null=True)
    season = models.CharField(max_length=20, choices=SEAS_CHOICES, blank=True, null=True)
    year = models.IntegerField(default=0)
    comfort = models.IntegerField(choices=COMFORT_CHOICES, blank=True, null=True)
    plant_fit = models.CharField(max_length=30, choices=PLANT_FIT_CHOICES, blank=True, null=True)
    state = models.CharField(max_length=30, choices=STATE_CHOICES, blank=True, null=True)
    available = models.BooleanField(default=True)
    info = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    favourite = models.BooleanField(default=False)
    cart = models.BooleanField(default=False)
    ordered = models.IntegerField(default=0, blank=True, null=True)
    urgent = models.BooleanField(default=False)
    delivered_date = models.CharField(max_length=200, blank=True, null=True)
    returned_date = models.CharField(max_length=200, blank=True, null=True)
    def real_heel(self):
        return self.heel_height - self.plateau_height


    def checkItemState(self, user):
        state = ''
        if not self.available:
            state = 'in service'
        elif self.terminated_user.filter(pk=user.pk).exists():
            state = 'terminated'
        elif self.delivered_user.filter(pk=user.pk).exists():
            state = 'delivered'
        elif self.ordered_user.filter(pk=user.pk).exists():
            state = 'ordered'
        elif self.terminated_user.all():
            state = 'others have this'
        elif self.delivered_user.all():
            state = 'others have this'
        elif self.ordered_user.all():
            state = 'ordered by others'

        return state

class ShoeImage(models.Model):
    shoe = models.ForeignKey('Shoe', on_delete=models.CASCADE, null=True)
    image = models.ImageField()

class ShoeBrand(models.Model):
    brand = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.brand

from django.contrib.auth.models import User

class AccountConfig(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_config')
    dark_mode = models.BooleanField(default=False)

    PAGINATE_NUM = (
        (8, "8"),
        (32, "32"),
        (128, "128"),
        (0, "all"),
    )
    paginate = models.IntegerField(choices=PAGINATE_NUM, default=8, blank=False, null=False)
