# Generated by Django 5.1 on 2024-08-26 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_listing_brand_listing_color_listing_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='color',
            field=models.CharField(max_length=24),
        ),
    ]
