from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Program(models.Model):
    """
    A class representing a program/initiative to provide a service to patients.
    """
    name = models.CharField(verbose_name="Program name", unique=True, max_length=100,
                            help_text='The unique title for the program')
    description = models.TextField(verbose_name="Description", blank=True, null=True,
                                   help_text='The purpose of the program. This field is optional')
    date_created = models.DateField(auto_now_add=True, help_text='The date the program was first saved into the system')
    date_last_modified = models.DateField(auto_now=True,
                                          help_text='The most recent date any of the fields of the program was updated')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_programs', related_query_name='created_program',
                                   help_text='The user that add this program to the system')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='modified_programs', related_query_name='modified_program',
                                         help_text='The user that made the most recent update to any of the program '
                                                   'fields')

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('programs_program_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('programs_program_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('programs_program_delete', kwargs={'pk':self.pk})