# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-27 12:13
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20180627_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='Username must be lowercased and Alphanumeric', regex='^[a-z0-9]+$')], verbose_name='username'),
        ),
    ]
