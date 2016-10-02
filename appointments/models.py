from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from patients.models import Patient


class Appointment(models.Model):
    """
    A model representing an appointment a user schedules with a patient.
    """
    title = models.CharField(verbose_name='Title', max_length=100, help_text='A title to describe the appointment')
    notes = models.TextField(verbose_name='Notes', blank=True, null=True,
                             help_text='Any comments on this appointment. This field is optional')
    patient = models.ForeignKey(Patient, verbose_name='Patient', blank=True, null=True, on_delete=models.SET_NULL,
                                related_name='appointments', related_query_name='appointment',
                                help_text='The patient whom the user is scheduled to meet with. This field is optional '
                                          'but recommended')
    owner = models.ForeignKey(User, verbose_name='Appointment owner', blank=True, null=True, on_delete=models.SET_NULL,
                              related_name='owned_appointments', related_query_name='owned_appointment',
                              help_text='The user that is to meet with the patient. If not supplied, this is set as the'
                                        ' user creating the appointment')
    appointment_date = models.DateField(verbose_name='Appointment date',
                                        help_text='The date the appointment is to take place')
    start_time = models.TimeField(verbose_name='Appointment start time',
                                  help_text='The time the appointment is scheduled to start')
    end_time = models.TimeField(verbose_name='Appointment end time',
                                help_text='The time the appointment is scheduled to end')
    created_by = models.ForeignKey(User, verbose_name='Created by', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='created_appointments', related_query_name='created_appointment',
                                   help_text='The user that created the appointment')
    last_modified_by = models.ForeignKey(User, verbose_name='Last modified by', on_delete=models.SET_NULL, null=True,
                                         blank=True, related_name='modified_appointments',
                                         related_query_name='modified_appointment')
    date_created = models.DateField(verbose_name='Date created', auto_now_add=True,
                                    help_text='The date the appointment was created')
    date_last_modified = models.DateField(verbose_name='Date last modified', auto_now=True,
                                          help_text='The date on which the appointment was last modified')

    def __str__(self):
        return self.title.capitalize()

    def get_absolute_url(self):
        return reverse('appointments_appointment_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('appointments_appointment_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('appointments_appointment_delete', kwargs={'pk':self.pk})