from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


from patients.models import Patient


class EmergencyContact(models.Model):
    """
    A model representing a contact to whom an email should be sent in case of certain adverse events
    """
    name = models.CharField(verbose_name='Name', max_length=100, help_text='The name of the emergency contact')
    email = models.EmailField(verbose_name='Email', help_text='The email address of the emergency contact')

    date_created = models.DateField(auto_now_add=True, help_text='The date the emergency contact was added to the '
                                                                 'system')
    date_last_modified = models.DateField(auto_now=True, help_text='The most recent date any of the information on this'
                                                                   ' emergency contact was modified')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_emergency_contacts',
                                   related_query_name='created_emergency_contact', help_text='The user that created the'
                                                                                             ' emergency contact')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='modified_emergency_contacts',
                                         related_query_name='modified_emergency_contact',
                                         help_text='The user that made the most recent modification to the information'
                                                   ' of this emergency contact')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('adverse_emergency_contact_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('adverse_emergency_contact_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('adverse_emergency_contact_delete', kwargs={'pk':self.pk})


class AdverseEventType(models.Model):
    """
    A model representing a category/type of adverse event
    """
    name = models.CharField(verbose_name='Adverse event type name', unique=True, max_length=100,
                            help_text='The unique name for the adverse event type')
    description = models.TextField(verbose_name='Description', blank=True, null=True,
                                   help_text='Information about this adverse event type. This field is optional.')
    emergency_contacts = models.ManyToManyField(EmergencyContact, verbose_name='Emergency contacts', blank=True,
                                                related_name='adverse_event_types',
                                                related_query_name='adverse_event_type',
                                                help_text='The emergency contacts that are to receive emails when '
                                                          'adverse events of this type are created')

    date_created = models.DateField(auto_now_add=True, help_text='The date the adverse event type was added to the '
                                                                 'system')
    date_last_modified = models.DateField(auto_now=True, help_text='The most recent date that any information on this '
                                                                   'adverse event type was last modified')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_adverse_event_types',
                                   related_query_name='created_adverse_event_type',
                                   help_text='The user that added this adverse event type to the system')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='modified_adverse_event_types',
                                         related_query_name='modified_adverse_event_type',
                                         help_text='The user to last modify information on this adverse event type')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('adverse_event_type_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('adverse_event_type_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('adverse_event_type_delete', kwargs={'pk':self.pk})


class AdverseEvent(models.Model):
    """
    A model representing an adverse event
    """
    patient = models.ForeignKey(Patient, verbose_name='Patient', on_delete=models.CASCADE, related_name='adverse_events',
                                related_query_name='adverse_event',
                                help_text='The patient whom the adverse event has occurred to')
    adverse_event_type = models.ForeignKey(AdverseEventType, verbose_name='Adverse event type', on_delete=models.CASCADE,
                                           related_name='adverse_events', related_query_name='adverse_event',
                                           help_text='The category of this adverse event')
    event_date = models.DateField(verbose_name='Event date', help_text='The date the adverse event occurred')
    notes = models.TextField(verbose_name='Notes', blank=True, null=True,
                             help_text='Any information with regards to this adverse event')

    date_created = models.DateField(auto_now_add=True, help_text='The date the adverse event was added to the system')
    date_last_modified = models.DateField(auto_now=True, help_text='The date that details of this adverse event were '
                                                                   'last modified')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_adverse_events', related_query_name='created_adverse_event',
                                   help_text='The user that added this adverse event to the system')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='modified_adverse_events',
                                         related_query_name='modified_adverse_event',
                                         help_text='The user that last modified the details of this adverse event')

    def __str__(self):
        temp_str = "{0} adverse event for {1} on {2}".format(self.adverse_event_type, self.patient.get_full_name(),
                                                             self.event_date)
        return temp_str

    def get_absolute_url(self):
        return reverse('adverse_event_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('adverse_event_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('adverse_event_delete', kwargs={'pk':self.pk})