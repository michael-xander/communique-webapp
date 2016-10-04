from django.db.models.signals import post_save
from django.dispatch import receiver

from communique.utils.utils_signals import send_notification
from .models import Event


@receiver(post_save, sender=Event)
def post_event_save_callback(sender, **kwargs):
    """
    Creates a notification informing all users about creation or editing of an event
    """
    event = kwargs['instance']

    # check whether the user responsible for saving the object is available
    if event.last_modified_by:
        # check whether the object was created or updated

        if kwargs['created']:
            temp_str = 'added'
        else:
            temp_str = 'updated'

        verb = "{0} the event:".format(temp_str)

        description = event.description

        send_notification(actor=event.last_modified_by, action_object=event, verb=verb, entity_name='event',
                          description=description)