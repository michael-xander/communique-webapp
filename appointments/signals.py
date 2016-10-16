from django.db.models.signals import post_save
from django.dispatch import receiver

from communique.utils.utils_signals import generate_notifications
from user.models import NotificationRegistration
from .models import Appointment


@receiver(post_save, sender=Appointment)
def post_appointment_save_callback(sender, **kwargs):
    """
    Creates a notification informing all users about the appointment
    """
    generate_notifications(NotificationRegistration.APPOINTMENTS, kwargs)