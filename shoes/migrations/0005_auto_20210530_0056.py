# Generated by Django 3.2 on 2021-05-29 22:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoes', '0004_auto_20210529_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='delivered_user',
            field=models.ManyToManyField(blank=True, related_name='delivered_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shoe',
            name='ordered_user',
            field=models.ManyToManyField(blank=True, related_name='ordered_items', to=settings.AUTH_USER_MODEL),
        ),
    ]
