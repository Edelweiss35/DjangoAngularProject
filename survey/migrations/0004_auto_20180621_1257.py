# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_survey_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='max',
            field=models.IntegerField(blank=True, default=2000, null=True, verbose_name='Max'),
        ),
        migrations.AddField(
            model_name='question',
            name='min',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Min'),
        ),
        migrations.AddField(
            model_name='question',
            name='placeholder',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='Placeholder'),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('para', 'text (multiple line)'), ('short', 'short text (one line)'), ('radio', 'radio'), ('checkbox', 'checkbox'), ('integer', 'integer'), ('dropbox', 'dropbox'), ('date', 'date'), ('time', 'time')], default='para', max_length=200, verbose_name='Type'),
        ),
    ]
