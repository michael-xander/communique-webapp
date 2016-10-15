from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from patients.models import Patient


class MedicalReportType(models.Model):
    """
    A model representing the type of a medical report.
    """
    name = models.CharField(verbose_name='Medical report type name', unique=True, max_length=100,
                            help_text='The name to give to this medical report type')
    description = models.TextField(verbose_name='Description', blank=True, null=True,
                                   help_text='The purpose of this medical report type. This field is optional')
    created_by = models.ForeignKey(User, verbose_name='Created by', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_medical_report_types',
                                   related_query_name='created_medical_report_type',
                                   help_text='The user that created this medical report type')
    last_modified_by = models.ForeignKey(User, verbose_name='Modified by', on_delete=models.SET_NULL, blank=True,
                                         null=True, related_name='modified_medical_report_types',
                                         related_query_name='modified_medical_report_type',
                                         help_text='The user to last modify this medical report type')
    date_created = models.DateField(verbose_name='Date created', auto_now_add=True,
                                    help_text='The date on which the medical report type was created')
    date_last_modified = models.DateField(verbose_name='Date last modified', auto_now=True,
                                           help_text='The date on which details of this medical report type were last '
                                                     'modified')

    def __str__(self):
        return self.name.capitalize()

    def get_absolute_url(self):
        return reverse('medical_report_type_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('medical_report_type_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('medical_report_type_delete', kwargs={'pk':self.pk})


class MedicalReport(models.Model):
    """
    A model representing a medical report.
    """
    title = models.CharField(verbose_name='Title', max_length=100, help_text='The title of this medical report')
    report_type = models.ForeignKey(MedicalReportType, verbose_name='Medical report type', on_delete=models.CASCADE,
                                    related_name='medical_reports', related_query_name='medical_report',
                                    help_text='The type of this medical report')
    patient = models.ForeignKey(Patient, verbose_name='Patient', on_delete=models.CASCADE,
                                related_name='medical_reports', related_query_name='medical_report',
                                help_text='The patient whom this medical report is for')
    notes = models.TextField(verbose_name='Notes', blank=True, null=True,
                             help_text='Information on the medical report. This field is optional')

    date_created = models.DateField(verbose_name='Date created', auto_now_add=True,
                                    help_text='The date on which this medical report was created')
    date_last_modified = models.DateField(verbose_name='Date last modified', auto_now=True,
                                          help_text='The date on which the details of this medical report were last '
                                                    'modified')

    created_by = models.ForeignKey(User, verbose_name='Created by', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_medical_reports', related_query_name='created_medical_report',
                                   help_text='The user that created this medical report')
    last_modified_by = models.ForeignKey(User, verbose_name='Last modified by', on_delete=models.SET_NULL, blank=True,
                                         null=True, related_name='modified_medical_reports',
                                         related_query_name='modified_medical_report',
                                         help_text='The user that last modified this medical report')

    def __str__(self):
        temp_str = "{0} report: {1}".format(self.report_type, self.title.capitalize())
        return temp_str

    def get_absolute_url(self):
        return reverse('medical_report_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('medical_report_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('medical_report_delete', kwargs={'pk':self.pk})
