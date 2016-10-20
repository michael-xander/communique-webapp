from django.test import TestCase
from django.core.urlresolvers import reverse

import datetime

from regimens.models import Drug, Regimen
from patients.models import Patient


class DrugTestCase(TestCase):
    """
    Test cases for the Drug model.
    """
    def setUp(self):
        self.drug = Drug.objects.create(name='Drug', description='A drug description')

    def test_str(self):
        """
        A test case for the __str__ method of the model
        """
        self.assertEqual(self.drug.__str__(), 'Drug')

    def test_get_absolute_url(self):
        """
        A method that tests the get_absolute_url method of a model
        """
        self.assertEqual(self.drug.get_absolute_url(), reverse('regimens_drug_detail',
                                                               kwargs={'pk':self.drug.pk}))

    def test_get_update_url(self):
        """
        A method that tests the get_update_url method of a model
        """
        self.assertEqual(self.drug.get_update_url(), reverse('regimens_drug_update',
                                                             kwargs={'pk':self.drug.pk}))

    def test_get_delete_url(self):
        """
        A method that tests the get_delete_url method of a model
        """
        self.assertEqual(self.drug.get_delete_url(), reverse('regimens_drug_delete',
                                                             kwargs={'pk':self.drug.pk}))


class RegimenTestCase(TestCase):
    """
    Test cases for the Regimen model
    """
    def setUp(self):
        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE, identifier='A001')
        self.regimen = Regimen.objects.create(patient=patient, notes='Sample notes', date_started=datetime.date.today())

    def test_str(self):
        """
        A test case for the __str__ method of the model
        """
        today = datetime.date.today()
        patient = self.regimen.patient
        self.assertEqual(self.regimen.__str__(), "{0}'s regimen that started on {1}".format(patient.get_full_name(),
                                                                                            today))

        self.regimen.date_ended = today
        self.assertEqual(self.regimen.__str__(), "{0}'s regimen that started on {1} and ended on {2}".format(
            patient.get_full_name(), today, today))

    def test_get_absolute_url(self):
        """
        A test case for the get_absolute_url method of the model
        """
        self.assertEqual(self.regimen.get_absolute_url(), reverse('regimens_regimen_detail',
                                                                  kwargs={'pk':self.regimen.pk}))

    def test_get_delete_url(self):
        """
        A test case for the get_delete_url method of the model
        """
        self.assertEqual(self.regimen.get_delete_url(), reverse('regimens_regimen_delete',
                                                                kwargs={'pk':self.regimen.pk}))

    def test_get_update_url(self):
        """
        A test case for the get_update_url method of the model
        """
        self.assertEqual(self.regimen.get_update_url(), reverse('regimens_regimen_update',
                                                                kwargs={'pk':self.regimen.pk}))