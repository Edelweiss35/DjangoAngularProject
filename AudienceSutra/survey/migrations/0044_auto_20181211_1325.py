# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-11 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0043_auto_20181211_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
