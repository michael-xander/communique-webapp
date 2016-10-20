from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Event(models.Model):
    """
    A model representing an  created by a user.
    """
    name = models.CharField(verbose_name='Name', max_length=100, help_text='A name for the event')
    description = models.TextField(verbose_name='Description', blank=True, null=True,
                                   help_text='An optional description for this event')
    event_date = models.DateField(verbose_name='Event date', help_text='The date the event is to take place')
    start_time = models.TimeField(verbose_name='Event start time', help_text='The time the event is to start')
    end_time = models.TimeField(verbose_name='Event end time', help_text='The time the event is to end')

    created_by = models.ForeignKey(User, verbose_name='Created by', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='created_events', related_query_name='created_event',
                                   help_text='The user that created the event')
    last_modified_by = models.ForeignKey(User, verbose_name='Last modified by', on_delete=models.SET_NULL, null=True,
                                         blank=True, related_name='modified_events', related_query_name='modified_event',
                                         help_text='The user to last modify the event details')
    date_created = models.DateField(verbose_name='Date created', auto_now_add=True,
                                    help_text='The date the event was created')
    date_last_modified = models.DateField(verbose_name='Date last modified', auto_now=True,
                                          help_text='The date on which the event was last modified')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('occasions_event_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('occasions_event_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('occasions_event_delete', kwargs={'pk':self.pk})