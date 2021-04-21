# Generated by Django 3.2 on 2021-04-21 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0018_auto_20210422_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='comfort',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='size',
            field=models.FloatField(blank=True, choices=[('30', '30'), ('30.5', '30.5'), ('31', '31'), ('31.5', '31.5'), ('32', '32'), ('32.5', '32.5'), ('33', '33'), ('33.5', '33.5'), ('34', '34'), ('34.5', '34.5'), ('35', '35'), ('35.5', '35.5'), ('36', '30'), ('36.5', '36.5'), ('37', '30'), ('37.5', '37.5'), ('38', '30'), ('38.5', '38.5'), ('39', '30'), ('39.5', '39.5'), ('40', '40'), ('40.5', '40.5'), ('41', '40'), ('41.5', '41.5'), ('42', '40'), ('42.5', '42.5'), ('43', '40'), ('43.5', '43.5'), ('44', '40'), ('44.5', '44.5'), ('45', '45')], null=True),
        ),
    ]
