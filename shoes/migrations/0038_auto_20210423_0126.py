# Generated by Django 3.2 on 2021-04-22 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0037_alter_shoe_material'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoe',
            old_name='material',
            new_name='lining_material',
        ),
        migrations.AddField(
            model_name='shoe',
            name='sole_material',
            field=models.CharField(blank=True, choices=[('Leather', 'Leather'), ('Rubber', 'Rubber'), ('Fabric', 'Fabric'), ('Microfibra', 'Microfibra'), ('Other', 'Other')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='shoe',
            name='upper_material',
            field=models.CharField(blank=True, choices=[('Leather', 'Leather'), ('Rubber', 'Rubber'), ('Fabric', 'Fabric'), ('Microfibra', 'Microfibra'), ('Other', 'Other')], max_length=30, null=True),
        ),
    ]