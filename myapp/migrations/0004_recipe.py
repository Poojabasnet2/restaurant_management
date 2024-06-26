# Generated by Django 5.0.2 on 2024-03-23 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_inventory_unit_price_remove_order_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.inventory')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='myapp.menu')),
            ],
        ),
    ]
