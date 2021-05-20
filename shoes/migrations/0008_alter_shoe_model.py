# Generated by Django 3.2 on 2021-05-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0007_shoe_urgent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='model',
            field=models.CharField(blank=True, choices=[('Décolleté', 'Décolleté'), ("D'Orsay", "D'Orsay"), ('V-neck', 'V-neck'), ('Mules', 'Mules'), ('Sabot', 'Sabot'), ('Clogs', 'Clogs'), ('Mocassins', 'Mocassins'), ('Brogues', 'Brogues'), ('Sandals', 'Sandals'), ('Ankle Boots', 'Ankle Boots'), ('Lace-up', 'Lace-up'), ('Gladiators', 'Gladiators'), ('Boots', 'Boots'), ('Ankle Boots', 'Ankle Boots'), ('Sock Boots', 'Sock Boots'), ('Cuissardes', 'Cuissardes'), ('Sneakers', 'Sneakers'), ('Pumps', 'Pumps'), ('T-Strap', 'T-Strap'), ('Cross-Strap', 'Cross-Strap'), ('Diagonal-Strap', 'Diagonal-Strap'), ('Ankle-Strap', 'Ankle-Strap'), ('Texas', 'Texas'), ('Beatles', 'Beatles'), ('Bikers', 'Bikers'), ('Mary Jane', 'Mary Jane'), ('Ballet Flats', 'Ballets Flats'), ('Ballroom Dance Shoes', 'Ballroom Dance Shoes'), ('Espadrille', 'Espadrille'), ('Fantasy', 'Fantasy'), ('Corset', 'Corset'), ('Cut Out', 'Cut Out'), ('Flip-flops', 'Flip-flops')], max_length=200, null=True),
        ),
    ]