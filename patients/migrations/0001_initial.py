# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-15 06:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateField(help_text='The date the patient was enrolled into the program.', verbose_name='Enrollment date')),
                ('comment', models.TextField(blank=True, help_text='A comment on the enrollment. This field is optional', null=True, verbose_name='comment')),
                ('date_created', models.DateField(auto_now_add=True, help_text='The date that this enrollment was added to the system')),
                ('date_last_modified', models.DateField(auto_now=True, help_text='The date the details of this enrollment were last modified')),
                ('created_by', models.ForeignKey(blank=True, help_text='The user that added this enrollment to the system', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_enrollments', related_query_name='created_enrollment', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, help_text='The user that last modified details on this enrollment', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_enrollments', related_query_name='modified_enrollment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outcome_date', models.DateField(help_text='The date the outcome for the patient was obtained', verbose_name='Outcome date')),
                ('notes', models.TextField(blank=True, help_text='Any information with regards to this patient outcome. This field is optional', null=True, verbose_name='Notes')),
                ('date_created', models.DateField(auto_now_add=True, help_text='The date the outcome was added to the system')),
                ('date_last_modified', models.DateField(auto_now=True, help_text='The date the details of this outcome were last modified')),
                ('created_by', models.ForeignKey(blank=True, help_text='The user that created this patient outcome', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_patient_outcomes', related_query_name='created_patient_outcome', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, help_text='The user that last modified details on this patient outcome', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_patient_outcomes', related_query_name='modified_patient_outcome', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OutcomeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The unique name for the patient outcome category', max_length=100, unique=True, verbose_name='Patient outcome name')),
                ('description', models.TextField(blank=True, help_text='Definition of this patient outcome. This patient is optional', null=True, verbose_name='Description')),
                ('date_created', models.DateField(auto_now_add=True, help_text='The date this patient outcome type was added to the system')),
                ('date_last_modified', models.DateField(auto_now=True, help_text='The most recent date that details on this outcome type were last modified')),
                ('created_by', models.ForeignKey(blank=True, help_text='The user that added this outcome type to the system', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_patient_outcome_types', related_query_name='created_patient_outcome_type', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, help_text='The user that last modified details on this outcome type', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_patient_outcome_types', related_query_name='modified_patient_outcome_type', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(help_text="The patient's last name", max_length=100, verbose_name='Last name')),
                ('other_names', models.CharField(help_text='The middle and first names of the patient', max_length=150, verbose_name='Names')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], help_text='The sex of the patient', max_length=1, verbose_name="Patient's sex")),
                ('birth_date', models.DateField(blank=True, help_text='Please use the following format: DD/MM/YYYY. This field is optional.', null=True, verbose_name='Birth Date')),
                ('identifier', models.CharField(help_text='The identifier used in the existing filing system', max_length=150, unique=True, verbose_name='Patient Identifier')),
                ('location', models.CharField(blank=True, help_text='The current residential address of the patient. This field is optional.', max_length=150, null=True, verbose_name="Patient's address")),
                ('contact_number', models.CharField(blank=True, help_text='The telephone/mobile number for the patient. This field is optional.', max_length=50, null=True, verbose_name='Contact number')),
                ('second_contact_number', models.CharField(blank=True, help_text='A second contact number for the patient. This field is optional', max_length=50, null=True, verbose_name='Second contact number')),
                ('third_contact_number', models.CharField(blank=True, help_text='A third contact number for the patient. This field is optional', max_length=50, null=True, verbose_name='Third contact number')),
                ('reference_health_centre', models.CharField(blank=True, help_text='The health centre to be contacted for more information. This field is optional.', max_length=150, null=True, verbose_name='Reference health centre')),
                ('interim_outcome', models.CharField(blank=True, max_length=200, null=True, verbose_name='Interim outcome')),
                ('treatment_start_date', models.DateField(blank=True, help_text='The date the patient started treatment', null=True, verbose_name='Treatment start date')),
                ('archived', models.BooleanField(default=False, help_text='Whether this patient has been archived', verbose_name='Archived')),
                ('date_created', models.DateField(auto_now_add=True, help_text='The date/time the patient was created.')),
                ('date_last_modified', models.DateField(auto_now=True, help_text="The last date/time the patient's information was modified.")),
                ('created_by', models.ForeignKey(blank=True, help_text='The user that created the patient.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_patients', related_query_name='created_patient', to=settings.AUTH_USER_MODEL)),
                ('enrolled_programs', models.ManyToManyField(related_name='enrolled_patients', related_query_name='enrolled_patient', through='patients.Enrollment', to='programs.Program')),
                ('last_modified_by', models.ForeignKey(blank=True, help_text="The last user to modify the patient's information.", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_patients', related_query_name='modified_patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='outcome',
            name='outcome_type',
            field=models.ForeignKey(help_text='The category of the patient outcome', on_delete=django.db.models.deletion.CASCADE, related_name='outcomes', related_query_name='outcome', to='patients.OutcomeType', verbose_name='Patient outcome category'),
        ),
        migrations.AddField(
            model_name='outcome',
            name='patient',
            field=models.ForeignKey(help_text='The patient whom the outcome is for', on_delete=django.db.models.deletion.CASCADE, related_name='outcomes', related_query_name='outcome', to='patients.Patient', verbose_name='Patient'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='patient',
            field=models.ForeignKey(help_text='The patient being enrolled into a program', on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', related_query_name='enrollment', to='patients.Patient', verbose_name='Patient'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='program',
            field=models.ForeignKey(help_text='The program to which a patient is enrolled', on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', related_query_name='enrollment', to='programs.Program', verbose_name='Program'),
        ),
    ]
