from django.db.models.signals import post_save
from django.dispatch import receiver

from communique.utils.utils_signals import generate_notifications
from user.models import NotificationRegistration
from .models import Program


@receiver(post_save, sender=Program)
def post_program_save_callback(sender, **kwargs):
    """
    Creates notifications for all users registered for these kind of notifications when a program is added/updated
    """
    generate_notifications(NotificationRegistration.PROGRAMS, kwargs)