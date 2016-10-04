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
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A name for the event', max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, help_text='An optional description for this event', null=True, verbose_name='Description')),
                ('event_date', models.DateField(help_text='The date the event is to take place', verbose_name='Event date')),
                ('start_time', models.TimeField(help_text='The time the event is to start', verbose_name='Event start time')),
                ('end_time', models.TimeField(help_text='The time the event is to end', verbose_name='Event end time')),
                ('date_created', models.DateField(auto_now_add=True, help_text='The date the event was created', verbose_name='Date created')),
                ('date_last_modified', models.DateField(auto_now=True, help_text='The date on which the event was last modified', verbose_name='Date last modified')),
                ('created_by', models.ForeignKey(blank=True, help_text='The user that created the event', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_events', related_query_name='created_event', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('last_modified_by', models.ForeignKey(blank=True, help_text='The user to last modify the event details', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_events', related_query_name='modified_event', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
        ),
    ]
