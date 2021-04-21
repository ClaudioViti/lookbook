# Generated by Django 3.2 on 2021-04-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0008_shoe_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='heel_height',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='plateau_height',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
