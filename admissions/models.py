from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from patients.models import Patient


class Admission(models.Model):
    """
    A model representing an admission of an patient into a hospital/health centre
    """
    patient = models.ForeignKey(Patient, verbose_name='Patient', related_name='admissions',
                                related_query_name='admission', on_delete=models.CASCADE,
                                help_text='The patient who has been admitted to a health centre')
    admission_date = models.DateField(verbose_name='Admission date',
                                      help_text='The date the patient was admitted to the health centre')
    discharge_date = models.DateField(verbose_name='Discharge date', blank=True, null=True,
                                      help_text='The date the patient was discharged from the health centre')
    health_centre = models.CharField(verbose_name='Health centre', max_length=100,
                                     help_text='The health centre where the patient has been admitted')
    notes = models.TextField(verbose_name='Notes', blank=True, null=True,
                             help_text='Any notes or comments on the admission. This field is optional')

    created_by = models.ForeignKey(User, verbose_name='Created by', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='created_admissions', related_query_name='created_admission',
                                   help_text='The user that created the admission')
    last_modified_by = models.ForeignKey(User, verbose_name='Last modified by', on_delete=models.SET_NULL, null=True,
                                         blank=True, related_name='last_modified_admissions',
                                         related_query_name='last_modified_admission',
                                         help_text='The user to last modify the details of this admission')

    date_created = models.DateField(verbose_name='Date created', auto_now_add=True,
                                    help_text='The date the admission was created')
    date_last_modified = models.DateField(verbose_name='Date last modified', auto_now=True,
                                          help_text='The date on which the details of this admission were last updated')

    def __str__(self):
        temp_str = "{0} to {1}".format(self.patient.get_full_name(), self.health_centre)
        return temp_str

    def get_absolute_url(self):
        return reverse('admissions_admission_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('admissions_admission_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('admissions_admission_delete', kwargs={'pk':self.pk})