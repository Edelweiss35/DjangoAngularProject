# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-06 16:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaillogs',
            name='sent_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 6, 16, 20, 4, 171276, tzinfo=utc)),
        ),
    ]
