# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-10 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0033_auto_20181006_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='respondentsurveyassign',
            name='status',
            field=models.CharField(choices=[('Assigned', 'Assigned'), ('Taken', 'Taken')], default='Assigned', max_length=50),
        ),
    ]
