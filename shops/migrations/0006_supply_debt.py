# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-12 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_auto_20180505_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='debt',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]