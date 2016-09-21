from django.test import TestCase

from user.forms import CommuniqueUserCreationForm


class CommuniqueUserCreationFormTestCase(TestCase):
    """
    Test cases for the user creation form
    """

    def test_name_validation(self):
        """
        Tests that the last name and first name of a user have to be supplied for input to be considered as valid
        """

        form = CommuniqueUserCreationForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        data = {'username':'jon_snow', 'password1':'p@55words', 'password2':'p@55words'}
        form = CommuniqueUserCreationForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

        data['first_name'] = 'Jon'

        form = CommuniqueUserCreationForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())

        data['last_name'] = 'Snow'

        form = CommuniqueUserCreationForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())