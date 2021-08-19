# Generated by Django 3.2 on 2021-08-19 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoes', '0003_alter_accountconfig_dark_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountconfig',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_config', to=settings.AUTH_USER_MODEL),
        ),
    ]
