# Generated by Django 3.2 on 2021-04-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0011_shoe_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]