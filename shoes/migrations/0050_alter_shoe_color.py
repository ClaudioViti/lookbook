# Generated by Django 3.2 on 2021-04-26 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0049_auto_20210426_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='color',
            field=models.CharField(blank=True, choices=[('Black', 'Black'), ('Gray', 'Gray'), ('White', 'White'), ('Brown', 'Brown'), ('Beige', 'Beige'), ('Red', 'Red'), ('Gold', 'Gold'), ('Yellow', 'Yellow'), ('Pink', 'Pink'), ('Green', 'Green'), ('Orange', 'Orange'), ('Fuchsia', 'Fuchsia'), ('Blue', 'Blue'), ('Azure', 'Azure'), ('Silver', 'Silver'), ('Purple', 'Purple'), ('Wheat', 'Wheat')], max_length=200, null=True),
        ),
    ]
