# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0008_auto_20180626_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responses',
            name='user',
            field=models.IntegerField(default=0, verbose_name='user'),
        ),
    ]
