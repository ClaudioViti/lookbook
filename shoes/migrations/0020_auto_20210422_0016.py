# Generated by Django 3.2 on 2021-04-21 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0019_auto_20210422_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='comfort',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='size',
            field=models.FloatField(blank=True, choices=[('30.0', '30.0'), ('30.5', '30.5'), ('31.0', '31.0'), ('31.5', '31.5'), ('32.0', '32.0'), ('32.5', '32.5'), ('33.0', '33.0'), ('33.5', '33.5'), ('34.0', '34.0'), ('34.5', '34.5'), ('35.0', '35.0'), ('35.5', '35.5'), ('36.0', '36.0'), ('36.5', '36.5'), ('37.0', '30.0'), ('37.5', '37.5'), ('38.0', '30.0'), ('38.5', '38.5'), ('39.0', '30.0'), ('39.5', '39.5'), ('40.0', '40.0'), ('40.5', '40.5'), ('41.0', '41.0'), ('41.5', '41.5'), ('42.0', '40.0'), ('42.5', '42.5'), ('43.0', '40.0'), ('43.5', '43.5'), ('44.0', '40.0'), ('44.5', '44.5'), ('45.0', '45.0')], null=True),
        ),
    ]
