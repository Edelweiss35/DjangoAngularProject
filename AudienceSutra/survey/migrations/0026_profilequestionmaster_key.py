# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-15 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0025_profilequestionanswers'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilequestionmaster',
            name='key',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
