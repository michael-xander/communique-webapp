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
    identifier = models.CharField(verbose_name="Patient Identifier", unique=True, max_length=150,
                                  help_text='The identifier used in the existing filing system')
    location = models.CharField(verbose_name="Patient's address", blank=True, null=True, max_length=150,
                                help_text='The current residential address of the patient. This field is optional.')
    contact_number = models.CharField(verbose_name='Contact number', blank=True, null=True, max_length=50,
                                      help_text='The telephone/mobile number for the patient. This field is optional.')
    second_contact_number = models.CharField(verbose_name='Second contact number', blank=True, null=True, max_length=50,
                                             help_text='A second contact number for the patient. This field is optional')
    third_contact_number = models.CharField(verbose_name='Third contact number', blank=True, null=True, max_length=50,
                                            help_text='A third contact number for the patient. This field is optional')

    reference_health_centre = models.CharField(verbose_name='Reference health centre', blank=True, null=True,
                                               max_length=150,
                                               help_text='The health centre to be contacted for more information. This '
                                                         'field is optional.')
    interim_outcome = models.CharField(verbose_name='Interim outcome', max_length=200, blank=True, null=True)
    treatment_start_date = models.DateField(verbose_name='Treatment start date', blank=True, null=True,
                                            help_text='The date the patient started treatment')
    archived = models.BooleanField(verbose_name='Archived', default=False,
                                   help_text='Whether this patient has been archived')

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

    def get_contact_update_url(self):
        return reverse('patients_patient_contact_update', kwargs={'pk':self.pk})

    def get_archive_url(self):
        return reverse('patients_patient_archive', kwargs={'pk':self.pk})

    def get_unarchive_url(self):
        return reverse('patients_patient_unarchive', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('patients_patient_delete', kwargs={'pk':self.pk})


class Enrollment(models.Model):
    """
    A model representing an enrollment between a patient and a program.
    """
    patient = models.ForeignKey(Patient, verbose_name='Patient', on_delete=models.CASCADE, related_name='enrollments',
                                related_query_name='enrollment', help_text='The patient being enrolled into a program')
    program = models.ForeignKey(Program, verbose_name='Program', on_delete=models.CASCADE, related_name='enrollments',
                                related_query_name='enrollment', help_text='The program to which a patient is enrolled')
    date_enrolled = models.DateField(verbose_name='date of enrollment',
                                     help_text='The date the patient was enrolled into the program.')
    comment = models.TextField(verbose_name='comment', blank=True, null=True,
                               help_text='A comment on the enrollment')

    date_created = models.DateField(auto_now_add=True, help_text='The date that this enrollment was added to the system')
    date_last_modified = models.DateField(auto_now=True,
                                          help_text='The date the details of this enrollment were last modified')

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_enrollments', related_query_name='created_enrollment',
                                   help_text='The user that added this enrollment to the system')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='modified_enrollments', related_query_name='modified_enrollment',
                                         help_text='The user that last modified details on this enrollment')

    def __str__(self):
        temp_str = "{0} into {1} on {2}".format(self.patient.get_full_name(), self.program, self.date_enrolled)
        return temp_str

    def get_absolute_url(self):
        return reverse('patients_enrollment_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('patients_enrollment_update', kwargs={'pk':self.pk})


class OutcomeType(models.Model):
    """
    A model representing the category of an outcome for a patient
    """
    name = models.CharField(verbose_name='Patient outcome name', unique=True, max_length=100,
                            help_text='The unique name for the patient outcome category')
    description = models.TextField(verbose_name='Description', help_text='Definition of this patient outcome')

    date_created = models.DateField(auto_now_add=True,
                                    help_text='The date this patient outcome type was added to the system')
    date_last_modified = models.DateField(auto_now=True,
                                          help_text='The most recent date that details on this outcome type were last '
                                                    'modified')

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_patient_outcome_types',
                                   related_query_name='created_patient_outcome_type',
                                   help_text='The user that added this outcome type to the system')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='modified_patient_outcome_types',
                                         related_query_name='modified_patient_outcome_type',
                                         help_text='The user that last modified details on this outcome type')

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('patients_outcome_type_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('patients_outcome_type_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('patients_outcome_type_delete', kwargs={'pk':self.pk})


class Outcome(models.Model):
    """
    A model representing the outcome of a patient on a particular day
    """
    patient = models.ForeignKey(Patient, verbose_name='Patient', on_delete=models.CASCADE, related_name='outcomes',
                                related_query_name='outcome', help_text='The patient whom the outcome is for')
    outcome_type = models.ForeignKey(OutcomeType, verbose_name='Patient outcome category', on_delete=models.CASCADE,
                                     related_name='outcomes', related_query_name='outcome',
                                     help_text='The category of the patient outcome')
    outcome_date = models.DateField(verbose_name='Outcome date',
                                    help_text='The date the outcome for the patient was obtained')
    notes = models.TextField(verbose_name='Notes', blank=True, null=True,
                             help_text='Any information with regards to this patient outcome. This field is optional')

    date_created = models.DateField(auto_now_add=True, help_text='The date the outcome was added to the system')
    date_last_modified = models.DateField(auto_now=True,
                                          help_text='The date the details of this outcome were last modified')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_patient_outcomes', related_query_name='created_patient_outcome',
                                   help_text='The user that created this patient outcome')
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='modified_patient_outcomes',
                                         related_query_name='modified_patient_outcome',
                                         help_text='The user that last modified details on this patient outcome')

    def __str__(self):
        temp_str = "{0} outcome for {1} on {2}".format(self.outcome_type, self.patient.get_full_name(),
                                                       self.outcome_date)
        return temp_str

    def get_absolute_url(self):
        return reverse('patients_outcome_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('patients_outcome_update', kwargs={'pk':self.pk})

