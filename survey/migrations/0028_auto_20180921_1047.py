# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-21 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0027_survey_survey_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='is_published',
        ),
        migrations.AddField(
            model_name='survey',
            name='created_on',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Active', 'Active'), ('Inactive', 'Inactive')], default='Draft', max_length=20),
        ),
    ]
