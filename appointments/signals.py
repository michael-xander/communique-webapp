from django.db.models.signals import post_save
from django.dispatch import receiver

from communique.utils.utils_signals import send_notification
from .models import Appointment


@receiver(post_save, sender=Appointment)
def post_appointment_save_callback(sender, **kwargs):
    """
    Creates a notification informing all users about the appointment
    """
    appointment = kwargs['instance']

    # check whether user responsible for saving the object is available
    if appointment.last_modified_by:
        # check whether the object was created or updated

        if kwargs['created']:
            temp_str = 'added'
        else:
            temp_str = 'updated'

        verb = "{0} the appointment:".format(temp_str)

        description = appointment.notes

        send_notification(actor=appointment.last_modified_by, action_object=appointment, verb=verb,
                          entity_name='appointment', description=description)