from django.contrib.auth.models import User
from django.test import TestCase


class ViewsTestCase(TestCase):
    """
    A class containing generic tests that are utilised throughout the different view tests.
    """
    def setUp(self):
        """
        Set up users to be used throughout testing.
        """
        # by default, a created user is active
        self.active_user = User.objects.create_user(username='active_user', email='activeuser@gmail.com',
                                                    password='p@55words')
        self.inactive_user = User.objects.create_user(username='inactive_user', email='inactiveuser@gmail.com',
                                                 password='p@55words')
        self.inactive_user.is_active = False
        self.inactive_user.save()
        # create a superuser
        self.super_user = User.objects.create_superuser(username='super_user', email='superuser@gmail.com',
                                                        password='p@55words')

    def only_active_user_access_test(self, view_url, template_name):
        """
        Tests that only active users have access to this view.
        :param view_url: The url of the view being tested.
        :param template_name: The name of the template for the view being tested.
        """
        active_user = self.active_user
        self.assertTrue(active_user.is_active)
        self.client.force_login(active_user)
        response = self.client.get(view_url, follow=True)
        self.assertTemplateUsed(response, template_name)
        self.client.logout()

        inactive_user = self.inactive_user
        self.assertFalse(inactive_user.is_active)
        self.client.force_login(inactive_user)
        response = self.client.get(view_url, follow=True)
        self.assertTemplateUsed(response, 'user/login.html')

    def only_active_super_user_access_test(self, view_url, template_name):
        """
        Tests that only active superusers have access to this view
        :param view_url: The url of the view being tested
        :param template_name: The name of the template for the view being tested
        """
        super_user = self.super_user
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_superuser)
        self.client.force_login(super_user)
        response = self.client.get(view_url, follow=True)
        self.assertTemplateUsed(response, template_name)
        self.client.logout()

        active_user = self.active_user
        self.assertTrue(active_user.is_active)
        self.assertFalse(active_user.is_superuser)
        self.client.force_login(active_user)
        response = self.client.get(view_url, follow=True)
        self.assertTemplateUsed(response, 'user/login.html')