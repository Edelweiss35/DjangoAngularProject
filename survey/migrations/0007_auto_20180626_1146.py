# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20180626_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='user',
            field=models.TextField(default=0, verbose_name='user'),
        ),
    ]
