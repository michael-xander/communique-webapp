from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class CommuniqueUser(User):
    """
    A proxy model for the default User model, adding extra methods.
    """
    class Meta:
        proxy = True

    def get_absolute_url(self):
        return reverse('user_communique_user_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('user_communique_user_update', kwargs={'pk':self.pk})


class Profile(User):
    """
    A proxy model for the default User model, masquerading as a Profile.
    """
    class Meta:
        proxy = True

    def get_absolute_url(self):
        return reverse('user_profile_detail', kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('user_profile_update', kwargs={'pk':self.pk})


class NotificationRegistration(models.Model):
    """
    A class representing a registration for service notifications
    """
    ADMISSIONS = 'AD'
    ADVERSE_EVENTS = 'AE'
    APPOINTMENTS = 'AP'
    COUNSELLING_SESSIONS = 'CS'
    MEDICAL_REPORTS = 'MR'
    EVENTS = 'EV'
    PATIENTS = 'PA'
    PATIENT_OUTCOMES = 'PO'
    ENROLLMENTS = 'EN'
    PROGRAMS = 'PR'
    REGIMENS = 'RE'

    SERVICE_CHOICES = (
        (ADMISSIONS, 'Admissions'),
        (ADVERSE_EVENTS, 'Adverse Events'),
        (APPOINTMENTS, 'Appointments'),
        (COUNSELLING_SESSIONS, 'Counselling Sessions'),
        (MEDICAL_REPORTS, 'Medical Reports'),
        (EVENTS, 'Events'),
        (PATIENTS, 'Patients'),
        (PATIENT_OUTCOMES, 'Patient Outcomes'),
        (ENROLLMENTS, 'Enrollments'),
        (PROGRAMS, 'Programs'),
        (REGIMENS, 'Regimens'),
    )

    service = models.CharField(verbose_name='Service', max_length=2, choices=SERVICE_CHOICES,
                               help_text='The system service for which to receive notifications')
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE,
                             related_name='notification_registrations', related_query_name='notification_registration',
                             help_text='The user whom this notification registration is for')

    def __str__(self):
        return self.get_service_display()

    def get_delete_url(self):
        return reverse('user_notification_registration_delete', kwargs={'pk':self.pk})