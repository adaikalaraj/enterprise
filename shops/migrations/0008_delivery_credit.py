# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-12 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0007_supply_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='credit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
