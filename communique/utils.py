from django.contrib.auth.models import User
from django.test import TestCase

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


class ViewsTestCase(TestCase):
    """
    A class containing generic tests that are utilised throughout the different view tests.
    """
    def setUp(self):
        """
        Set up users to be used throughout testing.
        """
        # by default, a created user is active
        User.objects.create_user(username='active_user', email='activeuser@gmail.com', password='p@55words')
        inactive_user = User.objects.create_user(username='inactive_user', email='inactiveuser@gmail.com',
                                                 password='p@55words')
        inactive_user.is_active = False
        inactive_user.save()

    def only_active_user_access_test(self, view_url, template_name):
        """
        Tests that only active users have access to this view.
        :param view_url: The url of view being tested.
        :param template_name: The name of the template for the view being tested.
        """
        active_user = User.objects.get(username='active_user')
        self.assertTrue(active_user.is_active)
        self.client.force_login(active_user)
        response = self.client.get(view_url, follow=True)
        self.assertTemplateUsed(response, template_name)
        self.client.logout()

        inactive_user = User.objects.get(username='inactive_user')
        self.assertFalse(inactive_user.is_active)
        self.client.force_login(inactive_user)
        response = self.client.get(view_url, follow=True)
        self.assertTemplateUsed(response, 'user/login.html')