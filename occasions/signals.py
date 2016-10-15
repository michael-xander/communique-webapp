from django.db.models.signals import post_save
from django.dispatch import receiver

from communique.utils.utils_signals import generate_notifications
from user.models import NotificationRegistration
from .models import Event


@receiver(post_save, sender=Event)
def post_event_save_callback(sender, **kwargs):
    """
    Creates a notification informing all users about creation or editing of an event
    """
    generate_notifications(NotificationRegistration.EVENTS, kwargs)