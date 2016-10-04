# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-02 17:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The unique name of the drug', max_length=100, unique=True, verbose_name='Drug name')),
                ('description', models.TextField(help_text='Information about the drug', verbose_name='Description')),
                ('date_created', models.DateField(auto_now_add=True, help_text='The date the drug was added to the system')),
                ('date_last_modified', models.DateField(auto_now=True, help_text='The most recent date any of the information of this drug was last modified')),
                ('created_by', models.ForeignKey(blank=True, help_text='The user that added this drug to the system', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_drugs', related_query_name='created_drug', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, help_text='The user that made the most recent modification to any of the fields of this drug', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_drugs', related_query_name='modified_drug', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Regimen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(help_text='Any notes to be made on this regimen', verbose_name='Notes')),
                ('date_started', models.DateField(help_text='The date the patient started this regimen', verbose_name='Regimen start date')),
                ('date_ended', models.DateField(blank=True, help_text='The date the patient stopped this regimen. This field is optional', null=True, verbose_name='Regimen end date')),
                ('date_created', models.DateField(auto_now_add=True, help_text='The date the regimen was added to the system')),
                ('date_last_modified', models.DateField(auto_now=True, help_text='The date details of this regimen were most recently updated')),
                ('created_by', models.ForeignKey(blank=True, help_text='The user that added this regimen to the system', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_regimens', related_query_name='created_regimen', to=settings.AUTH_USER_MODEL)),
                ('drugs', models.ManyToManyField(related_name='regimens', related_query_name='regimen', to='regimens.Drug')),
                ('last_modified_by', models.ForeignKey(blank=True, help_text='The user that last modified details of this regimen', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_regimens', related_query_name='modified_regimen', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(help_text='The patient undertaking this regimen', on_delete=django.db.models.deletion.CASCADE, related_name='regimens', related_query_name='regimen', to='patients.Patient')),
            ],
            options={
                'ordering': ['-date_started', '-date_ended'],
            },
        ),
    ]
