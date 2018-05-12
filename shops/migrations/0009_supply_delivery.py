# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-12 08:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0008_delivery_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='delivery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supply', to='shops.Delivery'),
        ),
    ]
