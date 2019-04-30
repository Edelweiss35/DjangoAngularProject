# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-03 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0011_question_tab_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='dependent_option',
            field=models.TextField(blank=True, null=True, verbose_name='tabNames'),
        ),
        migrations.AlterField(
            model_name='question',
            name='dependent_question',
            field=models.TextField(blank=True, null=True, verbose_name='tabNames'),
        ),
    ]
