# Generated by Django 5.0.2 on 2024-03-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_inventory_unit_price_order_table_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='unit_price',
            field=models.IntegerField(),
        ),
    ]
