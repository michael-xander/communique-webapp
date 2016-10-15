from django.db.models.signals import post_save
from django.dispatch import receiver

from communique.utils.utils_signals import generate_notifications
from user.models import NotificationRegistration
from .models import Patient, Enrollment, Outcome


@receiver(post_save, sender=Patient)
def post_patient_save_callback(sender, **kwargs):
    """
    Creates notifications for all users registered for patient notifications on the creation and updating of a patient
    """
    generate_notifications(NotificationRegistration.PATIENTS, kwargs)


@receiver(post_save, sender=Enrollment)
def post_enrollment_save_callback(sender, **kwargs):
    """
    Creates notifications for all users registered for enrollment notifications on creation/modification of enrollments
    """
    generate_notifications(NotificationRegistration.ENROLLMENTS, kwargs)


@receiver(post_save, sender=Outcome)
def post_patient_outcome_save_callback(sender, **kwargs):
    """
    Creates notifications for all users registered for patient outcome notifications on creation/modification of a
    patient outcome
    """
    generate_notifications(NotificationRegistration.PATIENT_OUTCOMES, kwargs)