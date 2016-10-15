from django.db.models.signals import post_save
from django.dispatch import receiver

from communique.utils.utils_signals import send_notification, get_users_to_notify
from user.models import NotificationRegistration
from .models import Patient, Enrollment


@receiver(post_save, sender=Patient)
def post_patient_save_callback(sender, **kwargs):
    """
    Creates a notification for all users on the creation and updating of a patient
    """
    patient = kwargs['instance']

    # check whether the user responsible for saving the object is available
    if patient.last_modified_by:
        # check whether the object was created or updated

        if kwargs['created']:
            temp_str = 'added'
        else:
            temp_str = 'updated'

        verb = "{0} the patient:".format(temp_str)
        user_list = get_users_to_notify(NotificationRegistration.PATIENTS)

        send_notification(actor=patient.last_modified_by, action_object=patient, verb=verb, entity_name='patient',
                          all_users=False, user_list=user_list)


@receiver(post_save, sender=Enrollment)
def post_enrollment_save_callback(sender, **kwargs):
    """
    Creates a notification for all users on creation of an enrollment
    """
    enrollment = kwargs['instance']

    # check whether the user responsible for saving the object is available
    if enrollment.last_modified_by and kwargs['created']:
        verb = "added the enrollment:"

        send_notification(actor=enrollment.last_modified_by, action_object=enrollment, verb=verb, entity_name='enrollment',
                          description=enrollment.comment)
