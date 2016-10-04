from django.test import TestCase

from user.forms import CommuniqueUserCreationForm, ProfileUpdateForm


class CommuniqueUserCreationFormTestCase(TestCase):
    """
    Test cases for the user creation form
    """

    def test_first_name_validation(self):
        """
        Tests that form invalidates data with a first name provided
        """

        form = CommuniqueUserCreationForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        data = {'username':'jon_snow', 'password1':'p@55words', 'password2':'p@55words', 'last_name':'Snow'}
        form = CommuniqueUserCreationForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

        data['first_name'] = 'Jon'

        form = CommuniqueUserCreationForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

    def test_last_name_validation(self):
        """
        Tests that form invalidates data without a last name provided
        """
        form = CommuniqueUserCreationForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        data = {'username':'jon_snow', 'password1':'p@55words', 'password2':'p@55words', 'first_name':'Jon'}
        form = CommuniqueUserCreationForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

        data['last_name'] = 'Snow'

        form = CommuniqueUserCreationForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())


class ProfileUpdateFormTestCase(TestCase):
    """
    Test cases for the profile update form
    """

    def test_first_name_validation(self):
        """
        Tests that form invalidates data without a first name provided
        """
        form = ProfileUpdateForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        data = {'last_name':'Snow'}

        form = ProfileUpdateForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

        data['first_name'] = 'Jon'

        form = ProfileUpdateForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

    def test_last_name_validation(self):
        """
        Tests that form invalidates data without last name provided
        """
        form = ProfileUpdateForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        data = {'first_name':'Jon'}

        form = ProfileUpdateForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

        data['last_name'] = 'Snow'

        form = ProfileUpdateForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())