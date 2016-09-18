from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from programs.models import Program


class Patient(models.Model):
    """
    A class representing a patient.
    """
    first_name = models.CharField(verbose_name="First name", max_length=100,
                                  help_text="The patient's first name. This field is required.")
    last_name = models.CharField(verbose_name="Last name", max_length=100,
                                 help_text="The patient's last name. This field is required.")
    middle_name = models.CharField(verbose_name="Middle name", blank=True, null=True, max_length=100,
                                   help_text="The patient's middle name. This field is optional.")

    birth_date = models.DateField(verbose_name="Birth Date", blank=True, null=True,
                                  help_text='Please use the following format: DD/MM/YYYY. This field is optional.')
    identifier = models.CharField(verbose_name="Patient Identifier", unique=True, blank=True, null=True, max_length=150,
                                  help_text='The identifier used in the existing filing system. This field is optional.')
    location = models.CharField(verbose_name="Patient location", blank=True, null=True, max_length=150,
                                help_text='The current residential address of the patient. This field is optional.')
    contact_number = models.CharField(verbose_name='Contact number', blank=True, null=True, max_length=50,
                                      help_text='The telephone/mobile number for the patient. This field is optional.')
    reference_health_centre = models.CharField(verbose_name='Reference health centre', blank=True, null=True,
                                               max_length=150,
                                               help_text='The health centre to be contacted for more information. This field is optional.')

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_patients', related_query_name='created_patient',
                                   help_text='The user that created the patient.')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='modified_patients', related_query_name='modified_patient',
                                         help_text="The last user to modify the patient's information.")

    date_created = models.DateField(auto_now_add=True, help_text='The date/time the patient was created.')
    date_last_modified = models.DateField(auto_now=True,
                                              help_text="The last date/time the patient's information was modified.")
    enrolled_programs = models.ManyToManyField(Program, through='Enrollment', related_name='enrolled_patients',
                                               related_query_name='enrolled_patient')

    def __str__(self):
        name = ''
        if self.middle_name:
            name = self.first_name + ' ' + self.middle_name + ' ' + self.last_name
        else:
            name = self.first_name + ' ' + self.last_name

        return name.title()

    def get_absolute_url(self):
        return reverse('patients_patient_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('patients_patient_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('patients_patient_delete', kwargs={'pk':self.pk})


class Enrollment(models.Model):
    """
    A model representing an enrollment between a patient and a program.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='enrollments',
                                related_query_name='enrollment', help_text='The patient enrolled in the program.')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='enrollments',
                                related_query_name='enrollment', help_text='The program to which a patient is enrolled')
    date_enrolled = models.DateField(verbose_name='date of enrollment', auto_now_add=True,
                                     help_text='The date the patient was enrolled into the program.')
    enrolled_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='registered_enrollments', related_query_name='registered_enrollment',
                                    help_text="The user that registers a patient's enrollment into a program.")
    comment = models.TextField(verbose_name='comment', help_text='A comment on the enrollment')
    is_active = models.BooleanField(verbose_name='is open', default=True,
                                    help_text='Whether this enrollment is still active.')

    def __str__(self):
        temp_str = "{0} into {1}".format(self.patient, self.program)
        return temp_str

    def get_absolute_url(self):
        return reverse('patients_enrollment_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('patients_enrollment_update', kwargs={'pk':self.pk})


