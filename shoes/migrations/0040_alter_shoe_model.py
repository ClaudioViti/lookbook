# Generated by Django 3.2 on 2021-04-23 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0039_alter_shoe_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='model',
            field=models.CharField(blank=True, choices=[('Décolleté', 'Décolleté'), ('Mules', 'Mules'), ('Sabot', 'Sabot'), ('Clogs', 'Clogs'), ('Mocassins', 'Mocassins'), ('Brogues', 'Brogues'), ('Open Toe', 'Open Toe'), ('Sandals', 'Sandals'), ('Wedges', 'Wedges'), ('Platform', 'Platform'), ('Ankle Boots', 'Ankle Boots'), ('Lace-up', 'Lace-up'), ('Gladiators', 'Gladiators'), ('Boots', 'Boots'), ('Sneakers', 'Sneakers'), ('Pumps', 'Pumps'), ('T-Strap', 'T-Strap'), ('Ankle-Strap', 'Ankle-Strap'), ('Texas', 'Texas')], max_length=200, null=True),
        ),
    ]
