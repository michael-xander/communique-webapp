from django.test import TestCase
from django.core.urlresolvers import reverse

from user.models import CommuniqueUser, Profile, NotificationRegistration, User


class CommuniqueUserTestCase(TestCase):
    """
    Test cases for the CommuniqueUser model.
    """
    def setUp(self):
        self.user = CommuniqueUser.objects.create_superuser('jon_snow', 'jonsnow@gmail.com', 'p@55words')

    def test_get_absolute_url(self):
        """
        Tests that the right url path is returned to obtain the details of a Communiqué user.
        """
        self.assertEqual(self.user.get_absolute_url(), reverse('user_communique_user_detail', kwargs={'pk':self.user.pk}))

    def test_get_update_url(self):
        """
        Tests that the right url path is returned to update a Communiqué user.
        """
        self.assertEqual(self.user.get_update_url(), reverse('user_communique_user_update', kwargs={'pk':self.user.pk}))


class ProfileTestCase(TestCase):
    """
    Test cases for the Profile model.
    """
    def setUp(self):
        self.profile = Profile.objects.create_superuser('jon_snow', 'jonsnow@gmail.com', 'p@55words')

    def test_get_absolute_url(self):
        """
        Tests that the right url path is returned to obtain the details of a Profile.
        """
        self.assertEqual(self.profile.get_absolute_url(), reverse('user_profile_detail', kwargs={'pk':self.profile.pk}))

    def test_get_update_url(self):
        """
        Tests that the right url path is returned to update the details of a Profile.
        """
        self.assertEqual(self.profile.get_update_url(), reverse('user_profile_update', kwargs={'pk':self.profile.pk}))


class NotificationRegistrationTestCase(TestCase):
    """
    Test cases for the NotificationRegistration model
    """
    def setUp(self):
        user = User.objects.create_user(username='user', email='user@gmail.com', password='p@55words')
        self.registration = NotificationRegistration.objects.create(service=NotificationRegistration.ADMISSIONS,
                                                                    user=user)

    def test_str(self):
        """
        Test the __str__ method of the model
        """
        self.assertEqual(self.registration.__str__(), self.registration.get_service_display())