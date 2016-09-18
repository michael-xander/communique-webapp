from django.test import TestCase
from django.core.urlresolvers import reverse

import datetime

from admissions.models import Admission
from patients.models import Patient


class AdmissionTestCase(TestCase):
    """
    Test cases for the Admission model.
    """
    def setUp(self):
        patient = Patient.objects.create(first_name='Jon', last_name='Snow')
        Admission.objects.create(patient=patient, admission_date=datetime.date.today(), health_centre="St.Michael's")

    def test_str(self):
        """
        A test case for the string method of the model
        """
        admission = Admission.objects.get(id=1)
        self.assertEqual(admission.__str__(), "Jon Snow to St.Michael's")
        
    def test_get_absolute_url(self):
        """
        A test case for the get_absolute_url method of the model.
        """
        admission = Admission.objects.get(id=1)
        self.assertEqual(admission.get_absolute_url(), reverse('admissions_admission_detail',
                                                               kwargs={'pk':admission.pk}))

    def test_get_update_url(self):
        """
        A test case of the get_update_url method of the model.
        """
        admission = Admission.objects.get(id=1)
        self.assertEqual(admission.get_update_url(), reverse('admissions_admission_update', kwargs={'pk':admission.pk}))

    def test_get_delete_url(self):
        """
        A test case of the get_delete_url method of the model.
        """
        admission = Admission.objects.get(id=1)
        self.assertEqual(admission.get_delete_url(), reverse('admissions_admission_delete', kwargs={'pk':admission.pk}))