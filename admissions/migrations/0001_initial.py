# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-18 08:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_date', models.DateField(help_text='The date the patient was admitted to the health centre', verbose_name='Admission date')),
                ('discharge_date', models.DateField(blank=True, help_text='The date the patient was discharged from the health centre', null=True, verbose_name='Discharge date')),
                ('health_centre', models.CharField(help_text='The health centre where the patient has been admitted', max_length=100, verbose_name='Health centre')),
                ('notes', models.TextField(blank=True, help_text='Any notes or comments on the admission. This field is optional', null=True, verbose_name='Notes')),
                ('date_created', models.DateField(auto_now_add=True, help_text='The date the admission was created', verbose_name='Date created')),
                ('date_last_modified', models.DateField(auto_now=True, help_text='The date on which the details of this admission were last updated', verbose_name='Date last modified')),
                ('created_by', models.ForeignKey(blank=True, help_text='The user that created the admission', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_admissions', related_query_name='created_admission', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('last_modified_by', models.ForeignKey(blank=True, help_text='The user to last modify the details of this admission', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_modified_admissions', related_query_name='last_modified_admission', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('patient', models.ForeignKey(help_text='The patient who has been admitted to a health centre', on_delete=django.db.models.deletion.CASCADE, related_name='admissions', related_query_name='admission', to='patients.Patient', verbose_name='Patient')),
            ],
        ),
    ]
