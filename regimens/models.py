from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from patients.models import Patient


class Drug(models.Model):
    """
    A class representing a drug that is added to a patient's regimen.
    """
    name = models.CharField(verbose_name='Drug name', unique=True, max_length=100,
                            help_text='The unique name of the drug')
    description = models.TextField(verbose_name='Description', help_text='Information about the drug')

    date_created = models.DateField(auto_now_add=True, help_text='The date the drug was added to the system')
    date_last_modified = models.DateField(auto_now=True, help_text='The most recent date any of the information of this'
                                                                   ' drug was last modified')

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='created_drugs',
                                  related_query_name='created_drug', help_text='The user that added this drug to the '
                                                                               'system')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='modified_drugs', related_query_name='modified_drug',
                                         help_text='The user that made the most recent modification to any of the fields'
                                                   ' of this drug')

    def save(self, *args, **kwargs):
        # store the name of the drug in lower case
        self.name = self.name.lower()
        super(Drug, self).save(*args, **kwargs)

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('regimens_drug_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('regimens_drug_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('regimens_drug_delete', kwargs={'pk':self.pk})


class Regimen(models.Model):
    """
    A class representing a regimen for a patient
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='regimens', related_query_name='regimen'
                                , help_text='The patient undertaking this regimen')
    notes = models.TextField(verbose_name='Notes', help_text='Any notes to be made on this regimen')
    drugs = models.ManyToManyField(Drug, related_name='regimens', related_query_name='regimen')
    date_started = models.DateField(verbose_name='Regimen start date', help_text='The date the patient started this '
                                                                                 'regimen')
    date_ended = models.DateField(verbose_name='Regimen end date', blank=True, null=True, help_text='The date the '
                                                                                                    'patient stopped '
                                                                                                    'this regimen. This '
                                                                                                    'field is optional')
    current_regimen = models.BooleanField(verbose_name='Current regimen', default=True, help_text='Mark this regimen as '
                                                                                                  'the current patient '
                                                                                                  'regimen or not. By '
                                                                                                  'default, it will be '
                                                                                                  'marked as the current'
                                                                                                  ' regimen')

    date_created = models.DateField(auto_now_add=True, help_text='The date the regimen was added to the system')
    date_last_modified = models.DateField(auto_now=True, help_text='The date details of this regimen were most recently '
                                                                   'updated')

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_regimens', related_query_name='created_regimen',
                                   help_text='The user that added this regimen to the system')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='modified_regimens', related_query_name='modified_regimen',
                                         help_text='The user that last modified details of this regimen')

    def __str__(self):
        if self.date_ended:
            temp_str = "{0}'s regimen that started on {1} and ended on {2}".format(self.patient.get_full_name(),
                                                                                   self.date_started, self.date_ended)
        else:
            temp_str = "{0}'s regimen that started on {1}".format(self.patient.get_full_name(), self.date_started)

        return temp_str

    def get_absolute_url(self):
        return reverse('regimens_regimen_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        pass

    def get_delete_url(self):
        return reverse('regimens_regimen_delete', kwargs={'pk':self.pk})