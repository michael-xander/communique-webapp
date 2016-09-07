# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 14:33
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
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='A title to describe the appointment', max_length=100, verbose_name='Title')),
                ('notes', models.TextField(blank=True, help_text='Any comments on this appointment. This field is optional', null=True, verbose_name='Notes')),
                ('appointment_date', models.DateField(help_text='The date the appointment is to take place', verbose_name='Appointment date')),
                ('start_time', models.TimeField(help_text='The time the appointment is scheduled to start', verbose_name='Appointment start time')),
                ('end_time', models.TimeField(help_text='The time the appointment is scheduled to end', verbose_name='Appointment end time')),
                ('date_created', models.DateField(auto_now_add=True, help_text='The date the appointment was created', verbose_name='Date created')),
                ('date_last_modified', models.DateField(auto_now=True, help_text='The date on which the appointment was last modified', verbose_name='Date last modified')),
                ('created_by', models.ForeignKey(blank=True, help_text='The user that created the appointment', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_appointments', related_query_name='created_appointment', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_appointments', related_query_name='modified_appointment', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('owner', models.ForeignKey(help_text='The user that is to meet with the patient. If not supplied, this is set as the user creating the appointment', on_delete=django.db.models.deletion.CASCADE, related_name='owned_appointments', related_query_name='owned_appointment', to=settings.AUTH_USER_MODEL, verbose_name='Appointment owner')),
                ('patient', models.ForeignKey(blank=True, help_text='The patient whom the user is scheduled to meet with. This field is optional but recommended', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointments', related_query_name='appointment', to='patients.Patient', verbose_name='Patient')),
            ],
        ),
    ]
