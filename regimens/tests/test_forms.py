from django.test import TestCase

import datetime

from regimens.forms import RegimenForm
from regimens.models import Drug
from patients.models import Patient


class RegimenFormTestCase(TestCase):
    """
    Test cases for the regimen create form.
    """
    def setUp(self):
        Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE, identifier='A001')
        Drug.objects.create(name='a Drug', description='A drug description')

    def test_date_validation(self):
        """
        Tests that the form invalidates submissions where the start date is greater then the end date
        """
        form = RegimenForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        current_date = datetime.date.today()
        one_day = datetime.timedelta(days=1)
        tomorrow = current_date + one_day

        data = {}
        data['patient'] = 1
        data['notes'] = 'Sample notes'
        data['drugs'] = (1,)
        data['date_started'] = current_date
        data['date_ended'] = tomorrow

        self.assertTrue(data['date_started'] < data['date_ended'])
        form = RegimenForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        data['date_started'] = tomorrow
        data['date_ended'] = current_date

        self.assertFalse(data['date_started'] < data['date_ended'])
        form = RegimenForm(data)
        self.assertTrue(data)
        self.assertFalse(form.is_valid())