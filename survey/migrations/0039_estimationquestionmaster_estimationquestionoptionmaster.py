# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-26 07:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0038_auto_20181013_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstimationQuestionMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('options_type', models.CharField(choices=[('Single Choice', 'Single Choice'), ('Multiple Choice', 'Multiple Choice'), ('Single Line Text', 'Single Line Text'), ('Multi Line Text', 'Multi Line Text'), ('Dropdown', 'Dropdown'), ('Date', 'Date')], max_length=100)),
                ('sort_order', models.IntegerField(default=0)),
                ('is_required', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EstimationQuestionOptionMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_detail', models.TextField(blank=True, default=None, null=True)),
                ('sort_order', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.EstimationQuestionMaster')),
            ],
        ),
    ]
