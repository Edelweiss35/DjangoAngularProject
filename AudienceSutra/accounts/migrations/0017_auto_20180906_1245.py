# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-06 12:45
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import utilities.jsonfield


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0016_auto_20180629_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=60, null=True)),
                ('company_name', models.CharField(blank=True, max_length=60, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('relationship_status', models.CharField(blank=True, max_length=30, null=True)),
                ('parential_status', models.IntegerField(blank=True, null=True)),
                ('child_age', utilities.jsonfield.JSONField(default={})),
                ('current_city', models.CharField(blank=True, max_length=30, null=True)),
                ('current_state', models.CharField(blank=True, max_length=30, null=True)),
                ('education', models.CharField(blank=True, max_length=30, null=True)),
                ('employment', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_birth', models.CharField(blank=True, max_length=30, null=True)),
                ('language_count', models.IntegerField(blank=True, null=True)),
                ('language_known', utilities.jsonfield.JSONField(default={})),
                ('family_count', models.IntegerField(blank=True, null=True)),
                ('household_income', models.CharField(blank=True, max_length=50, null=True)),
                ('earning_members_count', models.IntegerField(blank=True, null=True)),
                ('employment_position', models.CharField(blank=True, max_length=50, null=True)),
                ('work_sector', models.CharField(blank=True, max_length=50, null=True)),
                ('vehicle_count', models.IntegerField(blank=True, null=True)),
                ('vehicle_known', utilities.jsonfield.JSONField(default={})),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='last name')),
                ('middle_name', models.CharField(blank=True, max_length=35, null=True, verbose_name='middle name')),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(blank=True, max_length=60, null=True)),
                ('state', models.CharField(blank=True, max_length=60, null=True)),
                ('city', models.CharField(blank=True, max_length=60, null=True)),
                ('pincode', models.CharField(blank=True, max_length=6, null=True)),
                ('user_type', models.CharField(choices=[('Client', 'Client'), ('Respondent', 'Respondent')], max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='respondentprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='session',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='ClientProfile',
        ),
        migrations.DeleteModel(
            name='RespondentProfile',
        ),
        migrations.DeleteModel(
            name='Session',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
