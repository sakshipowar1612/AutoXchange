# Generated by Django 5.1 on 2024-08-24 04:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_location_pin_code_location_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.location'),
        ),
    ]