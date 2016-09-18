from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from patients.models import Patient


class CounsellingSessionType(models.Model):
    """
    A model representing the possible type of a counselling session.
    """
    name = models.CharField(verbose_name='Counselling session type', unique=True, max_length=100,
                            help_text='The name to be given to this counselling session type.')
    description = models.TextField(verbose_name='Description', blank=True, null=True,
                                   help_text='The description of this counselling session type. This field is optional.')
    date_created = models.DateField(verbose_name='Date created', auto_now_add=True,
                                    help_text='The date on which the counselling session type was created.')
    created_by = models.ForeignKey(User, verbose_name='Created by', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_counselling_session_types',
                                   related_query_name='created_counselling_session_type',
                                   help_text='The user that created the counselling session type')
    date_last_modified = models.DateField(verbose_name='Date last modified', auto_now=True,
                                          help_text='The date on which the counselling session type was last modified')
    last_modified_by = models.ForeignKey(User, verbose_name='Modified by', on_delete=models.SET_NULL, blank=True,
                                         null=True, related_name='modified_counselling_session_types',
                                         related_query_name='modified_counselling_session_type',
                                         help_text='The user to last modify the counselling session type')

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('counselling_sessions_type_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('counselling_sessions_type_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('counselling_sessions_type_delete', kwargs={'pk':self.pk})


class CounsellingSession(models.Model):
    """
    A model representing a session i.e an interaction between a patient and facilitator.
    """
    counselling_session_type = models.ForeignKey(CounsellingSessionType, verbose_name='Counselling session type',
                                                 on_delete=models.CASCADE, related_name='counselling_sessions',
                                                 related_query_name='counselling_session',
                                                 help_text='The category which this counselling session falls into')
    patient = models.ForeignKey(Patient, verbose_name='Patient', on_delete=models.CASCADE,
                                related_name='counselling_sessions', related_query_name='counselling_session',
                                help_text='The patient for whom the counselling session is for')
    notes = models.TextField(verbose_name='Notes', blank=True, null=True,
                             help_text='Any additional notes on the counselling session. This field is optional.')
    created_by = models.ForeignKey(User, verbose_name='Administered by', on_delete=models.SET_NULL, blank=True,
                                   null=True, related_name='created_counselling_sessions',
                                   related_query_name='created_counselling_session',
                                   help_text='The user that administered the counselling session')
    date_created = models.DateField(verbose_name='Date created', auto_now_add=True,
                                    help_text='The date on which the counselling session was created')
    last_modified_by = models.ForeignKey(User, verbose_name='Last modified by', on_delete=models.SET_NULL, blank=True,
                                         null=True, related_name='modified_counselling_sessions',
                                         related_query_name='modified_counselling_session',
                                         help_text='The user to last modify the counselling session')
    date_last_modified = models.DateField(verbose_name='Date last modified', auto_now=True,
                                          help_text='The date on which the counselling session was last modified')

    def __str__(self):
        return "A {0} session for {1}".format(self.counselling_session_type, self.patient.get_full_name())

    def get_absolute_url(self):
        return reverse('counselling_sessions_session_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('counselling_sessions_session_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('counselling_sessions_session_delete', kwargs={'pk':self.pk})



