from django.db.models.signals import post_save
from django.dispatch import receiver

from communique.utils.utils_signals import generate_notifications
from user.models import NotificationRegistration
from .models import Admission


@receiver(post_save, sender=Admission)
def post_admission_save_callback(sender, **kwargs):
    """
    Creates a notification informing all users about creation or editing of admission
    """
    generate_notifications(NotificationRegistration.ADMISSIONS, kwargs)

