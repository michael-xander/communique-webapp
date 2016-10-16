from django.db.models.signals import post_save
from django.dispatch import receiver

from communique.utils.utils_signals import generate_notifications
from user.models import NotificationRegistration
from .models import MedicalReport


@receiver(post_save, sender=MedicalReport)
def post_medical_report_save_callback(sender, **kwargs):
    """
    Creates notifications for all users registered for notifications when medical reports are added/updated
    """
    generate_notifications(NotificationRegistration.MEDICAL_REPORTS, kwargs)