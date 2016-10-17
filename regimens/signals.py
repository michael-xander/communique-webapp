from django.db.models.signals import post_save
from django.dispatch import receiver

from communique.utils.utils_signals import generate_notifications
from user.models import NotificationRegistration
from .models import Regimen


@receiver(post_save, sender=Regimen)
def post_regimen_save_callback(sender, **kwargs):
    """
    Creates notifications for all users registered for regimen notifications on addition/modification of a regimen
    """
    generate_notifications(NotificationRegistration.REGIMENS, kwargs)