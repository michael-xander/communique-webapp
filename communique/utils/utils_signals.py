from django.contrib.auth.models import User

from notifications.signals import notify


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
            notify.send(actor, recipient=notified_user, verb=verb, action_object=action_object, description=description,
                        entity_name=entity_name)
