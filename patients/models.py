from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from programs.models import Program


class Patient(models.Model):
    """
    A class representing a patient.
    """
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    last_name = models.CharField(verbose_name='Last name', max_length=100,
                                 help_text="The patient's last name")
    other_names = models.CharField(verbose_name='Names', max_length=150,
                                   help_text='The middle and first names of the patient')
    # there's a childish joke to be made here but it has been avoided to showcase maturity
    sex = models.CharField(verbose_name="Patient's sex", max_length=1, choices=SEX_CHOICES,
                           help_text='The sex of the patient')
    birth_date = models.DateField(verbose_name="Birth Date", blank=True, null=True,
                                  help_text='Please use the following format: DD/MM/YYYY. This field is optional.')
    identifier = models.CharField(verbose_name="Patient Identifier", unique=True, blank=True, null=True, max_length=150,
                                  help_text='The identifier used in the existing filing system')
    location = models.CharField(verbose_name="Patient's address", blank=True, null=True, max_length=150,
                                help_text='The current residential address of the patient. This field is optional.')
    contact_number = models.CharField(verbose_name='Contact number', blank=True, null=True, max_length=50,
                                      help_text='The telephone/mobile number for the patient. This field is optional.')
    reference_health_centre = models.CharField(verbose_name='Reference health centre', blank=True, null=True,
                                               max_length=150,
                                               help_text='The health centre to be contacted for more information. This field is optional.')
    interim_outcome = models.CharField(verbose_name='Interim outcome', max_length=200, blank=True, null=True)
    treatment_start_date = models.DateField(verbose_name='Treatment start date', blank=True, null=True,
                                            help_text='The date the patient started treatment')

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

    def get_full_name(self):
        temp_str = self.other_names + ' ' + self.last_name
        return temp_str.title()

    def __str__(self):
        temp_str = self.get_full_name()

        if self.identifier:
            temp_str = self.identifier + ' - ' + temp_str

        return temp_str

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


