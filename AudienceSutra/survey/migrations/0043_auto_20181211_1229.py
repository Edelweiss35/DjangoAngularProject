# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-11 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0042_survey_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True),
        ),
    ]
