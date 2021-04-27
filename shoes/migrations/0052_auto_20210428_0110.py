# Generated by Django 3.2 on 2021-04-27 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0051_alter_shoe_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='lining_material',
            field=models.CharField(blank=True, choices=[('Leather', 'Leather'), ('Patent leather', 'Patent leather'), ('Suede leather', 'Suede leather'), ('Rubber', 'Rubber'), ('Fabric', 'Fabric'), ('Wood', 'Wood'), ('Cork', 'Cork'), ('Synthetics', 'Synthetics'), ('Microfiber', 'Microfiber'), ('Plastic', 'Plastic'), ('Other', 'Other')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='sole_material',
            field=models.CharField(blank=True, choices=[('Leather', 'Leather'), ('Patent leather', 'Patent leather'), ('Suede leather', 'Suede leather'), ('Rubber', 'Rubber'), ('Fabric', 'Fabric'), ('Wood', 'Wood'), ('Cork', 'Cork'), ('Synthetics', 'Synthetics'), ('Microfiber', 'Microfiber'), ('Plastic', 'Plastic'), ('Other', 'Other')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='upper_material',
            field=models.CharField(blank=True, choices=[('Leather', 'Leather'), ('Patent leather', 'Patent leather'), ('Suede leather', 'Suede leather'), ('Rubber', 'Rubber'), ('Fabric', 'Fabric'), ('Wood', 'Wood'), ('Cork', 'Cork'), ('Synthetics', 'Synthetics'), ('Microfiber', 'Microfiber'), ('Plastic', 'Plastic'), ('Other', 'Other')], max_length=30, null=True),
        ),
    ]
