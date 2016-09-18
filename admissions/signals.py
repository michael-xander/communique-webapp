from django.db.models.signals import post_save
from django.dispatch import receiver

from communique.utils import send_notification
from .models import Admission


@receiver(post_save, sender=Admission)
def post_admission_save_callback(sender, **kwargs):
    """
    Creates a notification informing all users about creation or editing of admission
    """
    admission = kwargs['instance']

    # check whether the user responsible for saving the object is available
    if admission.last_modified_by:
        # check whether the object was created or updated

        if kwargs['created']:
            temp_str = 'added'
        else:
            temp_str = 'updated'

        verb = "{0} the admission:".format(temp_str)

        description = admission.notes

        send_notification(actor=admission.last_modified_by, action_object=admission, verb=verb, entity_name='admission',
                          description=description)

