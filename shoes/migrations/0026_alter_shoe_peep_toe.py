# Generated by Django 3.2 on 2021-04-21 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0025_auto_20210422_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='peep_toe',
            field=models.BooleanField(default=False),
        ),
    ]