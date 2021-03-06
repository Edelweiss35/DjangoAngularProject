# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 06:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20180629_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respondentprofile',
            old_name='childAge',
            new_name='child_age',
        ),
        migrations.RenameField(
            model_name='respondentprofile',
            old_name='currentCity',
            new_name='current_city',
        ),
        migrations.RenameField(
            model_name='respondentprofile',
            old_name='currentState',
            new_name='current_state',
        ),
        migrations.RenameField(
            model_name='respondentprofile',
            old_name='dateOfBirth',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='respondentprofile',
            old_name='earningMembersCount',
            new_name='earning_members_count',
        ),
        migrations.RenameField(
            model_name='respondentprofile',
            old_name='employmentPosition',
            new_name='employment_position',
        ),
        migrations.RenameField(
            model_name='respondentprofile',
            old_name='familyCount',
            new_name='family_count',
        ),
        migrations.RenameField(
            model_name='respondentprofile',
            old_name='householdIncome',
            new_name='household_income',
        ),
        migrations.RenameField(
            model_name='respondentprofile',
            old_name='languageCount',
            new_name='language_count',
        ),
        migrations.RenameField(
            model_name='respondentprofile',
            old_name='languageKnown',
            new_name='language_known',
        ),
        migrations.RenameField(
            model_name='respondentprofile',
            old_name='parentialStatus',
            new_name='parential_status',
        ),
        migrations.RenameField(
            model_name='respondentprofile',
            old_name='relationshipStatus',
            new_name='relationship_Status',
        ),
        migrations.RenameField(
            model_name='respondentprofile',
            old_name='vehicleCount',
            new_name='vehicle_count',
        ),
        migrations.RenameField(
            model_name='respondentprofile',
            old_name='vehicleKnown',
            new_name='vehicle_known',
        ),
        migrations.RenameField(
            model_name='respondentprofile',
            old_name='workSector',
            new_name='work_sector',
        ),
    ]
