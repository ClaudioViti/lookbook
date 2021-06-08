# Generated by Django 3.2 on 2021-06-05 01:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='delivered_user',
            field=models.ManyToManyField(blank=True, related_name='delivered_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shoe',
            name='favourite_user',
            field=models.ManyToManyField(blank=True, related_name='favourite_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shoe',
            name='ordered_user',
            field=models.ManyToManyField(blank=True, related_name='ordered_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shoe',
            name='urgent_user',
            field=models.ManyToManyField(blank=True, related_name='urgent_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='shoe',
            name='user',
        ),
        migrations.AddField(
            model_name='shoe',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='user_items', to=settings.AUTH_USER_MODEL),
        ),
    ]