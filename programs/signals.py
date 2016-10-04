from django.db.models.signals import post_save
from django.dispatch import receiver

from communique.utils.utils_signals import send_notification
from .models import Program


@receiver(post_save, sender=Program)
def post_program_save_callback(sender, **kwargs):
    """
    Creates a notification informing all users that a program has been added/edited.
    """
    program = kwargs['instance']

    # check whether the user responsible for saving the object is available
    if program.last_modified_by:
        # check whether the object was created or updated

        if kwargs['created']:
            verb = 'added'
        else:
            verb = 'updated'

        summary = "{0} the program:".format(verb)

        description = program.description

        send_notification(actor=program.last_modified_by, action_object=program, verb=summary, entity_name='program',
                          description=description)
