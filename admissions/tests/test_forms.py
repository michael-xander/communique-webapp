from django.test import TestCase

from admissions.forms import AdmissionCreateForm
from patients.models import Patient

import datetime


class AdmissionCreateFormTestCase(TestCase):
    """
    Test cases for the admission create form.
    """
    def setUp(self):
        Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE)

    def test_date_validation(self):
        """
        Tests that the form invalidates submissions where the admission date is greater than discharge date
        """
        form = AdmissionCreateForm()
        self.assertFalse(form.is_bound)
        self.assertFalse(form.is_valid())

        current_date = datetime.date.today()
        one_day = datetime.timedelta(days=1)
        tomorrow = current_date + one_day

        data = {}
        data['patient'] = 1
        data['health_centre'] = "St.Michael's hospital"
        data['notes'] = 'dummy notes'
        data['admission_date'] = current_date
        data['discharge_date'] = tomorrow

        self.assertTrue(data['admission_date'] < data['discharge_date'])
        form = AdmissionCreateForm(data)
        self.assertTrue(form.is_bound)
        self.assertTrue(form.is_valid())

        data['admission_date'] = tomorrow
        data['discharge_date'] = current_date

        self.assertFalse(data['admission_date'] < data['discharge_date'])
        form = AdmissionCreateForm(data)
        self.assertTrue(form.is_bound)
        self.assertFalse(form.is_valid())
