from django.test import TestCase

from counselling_sessions.forms import DurationForm

import datetime


class DurationFormTestCase(TestCase):
    """
    Test cases for the duration form
    """

    def test_date_validation(self):
        """
        Tests that the start date cannot be greater than the end date in the duration form
        """
        form = DurationForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        start_date = datetime.date.today()

        one_day = datetime.timedelta(days=1)

        end_date = start_date + one_day

        data = {'start_date':start_date, 'end_date':end_date}

        form = DurationForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        data['start_date'] = end_date
        data['end_date'] = start_date

        form = DurationForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())