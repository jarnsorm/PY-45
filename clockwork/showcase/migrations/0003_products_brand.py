# Generated by Django 5.0.4 on 2024-05-17 22:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0002_remove_products_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='showcase.brands'),
            preserve_default=False,
        ),
    ]
