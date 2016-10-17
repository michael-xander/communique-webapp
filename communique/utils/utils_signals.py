from django.contrib.auth.models import User
from user.models import NotificationRegistration
from fcm_django.models import FCMDevice
from notifications.signals import notify


def generate_notifications(service, given_kwargs):
    """
    A function to generate notifications for a service
    :param service: The service to generate notifications for
    :param given_kwargs: The kwargs provided when the post save signal for the service was called
    """
    model_instance = given_kwargs['instance']

    # check whether the user responsible for saving the object is available
    if model_instance.last_modified_by:
        actor = model_instance.last_modified_by
        action_object = model_instance

        # check whether the object was created or updated
        if given_kwargs['created']:
            temp_str = 'added'
        else:
            temp_str = 'updated'

        entity_name = ''
        description = None

        if service == NotificationRegistration.ADMISSIONS:
            entity_name = 'admission'
            description = model_instance.notes
        elif service == NotificationRegistration.ADVERSE_EVENTS:
            entity_name = 'adverse event'
            description = model_instance.notes
        elif service == NotificationRegistration.APPOINTMENTS:
            entity_name = 'appointment'
            description = model_instance.notes
        elif service == NotificationRegistration.COUNSELLING_SESSIONS:
            entity_name = 'counselling session'
            description = model_instance.notes
        elif service == NotificationRegistration.MEDICAL_REPORTS:
            entity_name = 'medical report'
            description = model_instance.notes
        elif service == NotificationRegistration.EVENTS:
            entity_name = 'event'
            description = model_instance.description
        elif service == NotificationRegistration.PATIENTS:
            entity_name = 'patient'
        elif service == NotificationRegistration.PATIENT_OUTCOMES:
            entity_name = 'patient outcome'
            description = model_instance.notes
        elif service == NotificationRegistration.ENROLLMENTS:
            entity_name = 'enrollment'
            description = model_instance.comment
        elif service == NotificationRegistration.PROGRAMS:
            entity_name = 'program'
            description = model_instance.description
        elif service == NotificationRegistration.REGIMENS:
            entity_name = 'regimen'
            description = model_instance.notes

        verb = '{0} the {1}:'.format(temp_str, entity_name)
        user_list = get_users_to_notify(service)

        send_notification(actor=actor, action_object=action_object, verb=verb, entity_name=entity_name,
                          description=description, all_users=False, user_list=user_list)


def send_notification(actor, action_object, verb, entity_name, description=None, all_users=True,
                      user_list=None):
    """
    A function to send a notification
    :param actor: The user that carried out the activity that other users are to be notified about
    :param action_object: The object linked to the activity carried out
    :param verb: The action taken by the actor
    :param description: The description of the notification
    :param entity_name: The class name of model the user interacted with
    :param all_users: Whether all users need be notified
    :param user_list: The list of users to be notified if not all users are to be notified
    """
    if all_users:
        notified_users = User.objects.all()
    else:
        notified_users = user_list

    for notified_user in notified_users:
        # only notify active users
        if notified_user.is_active:
            try:
                device = FCMDevice.objects.get(name=notified_user)
                device.send_message(data={"data": str(actor)+" "+str(verb) + " "+str(action_object)})
            except:
                print("Oops, this is embarassing!")
            notify.send(actor, recipient=notified_user, verb=verb, action_object=action_object, description=description,
                        entity_name=entity_name)


def get_users_to_notify(service):
    """
    A function to obtain the users to notify for a given service
    :param service: The service to notify users for
    :return: The list of users to notify
    """
    # get all the registrations for that service
    registrations = NotificationRegistration.objects.filter(service=service)

    user_list = []
    for registration in registrations:
        user_list.append(registration.user)

    return user_list

