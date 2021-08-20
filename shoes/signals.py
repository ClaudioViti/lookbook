from shoes.models import AccountConfig
from django.contrib.auth.models import User
from django.db.models.signals import post_save

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print('triggered')

        AccountConfig.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)