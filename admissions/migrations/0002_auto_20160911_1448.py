# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-11 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='discharge_date',
            field=models.DateField(blank=True, help_text='The date the patient was discharged from the health centre', null=True, verbose_name='Discharge date'),
        ),
    ]
