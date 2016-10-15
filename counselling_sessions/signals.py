from django.db.models.signals import post_save
from django.dispatch import receiver

from communique.utils.utils_signals import generate_notifications
from user.models import NotificationRegistration
from .models import CounsellingSession


@receiver(post_save, sender=CounsellingSession)
def post_counselling_session_save_callback(sender, **kwargs):
    """
    Creates notifications informing all users registered for the notifications that a counselling session been
    added/edited
    """
    generate_notifications(NotificationRegistration.COUNSELLING_SESSIONS, kwargs)