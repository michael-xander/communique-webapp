from django.db.models.signals import post_save
from django.dispatch import receiver

from communique.utils.utils_signals import generate_notifications
from user.models import NotificationRegistration
from .models import AdverseEvent


@receiver(post_save, sender=AdverseEvent)
def post_adverse_event_save_callback(sender, **kwargs):
    """
    Creates notifications informing all registered users that an adverse event has been created/updated
    """
    generate_notifications(NotificationRegistration.ADVERSE_EVENTS, kwargs)