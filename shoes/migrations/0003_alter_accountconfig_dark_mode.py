# Generated by Django 3.2 on 2021-08-18 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0002_auto_20210817_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountconfig',
            name='dark_mode',
            field=models.BooleanField(default=True),
        ),
    ]
