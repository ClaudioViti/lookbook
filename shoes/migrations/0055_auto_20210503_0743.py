# Generated by Django 3.2 on 2021-05-03 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0054_auto_20210429_0400'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoeImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='shoe',
            name='image',
        ),
        migrations.DeleteModel(
            name='Shoe_second_image',
        ),
        migrations.AddField(
            model_name='shoeimages',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.shoe'),
        ),
    ]
