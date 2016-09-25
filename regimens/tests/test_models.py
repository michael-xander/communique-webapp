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
        Drug.objects.create(name='a Drug', description='A drug description')

    def test_str(self):
        """
        A test case for the __str__ method of the model
        """
        drug = Drug.objects.get(id=1)
        self.assertEqual(drug.__str__(), 'A Drug')

    def test_get_absolute_url(self):
        """
        A method that tests the get_absolute_url method of a model
        """
        drug = Drug.objects.get(id=1)
        self.assertEqual(drug.get_absolute_url(), reverse('regimens_drug_detail', kwargs={'pk':drug.pk}))

    def test_get_update_url(self):
        """
        A method that tests the get_update_url method of a model
        """
        drug = Drug.objects.get(id=1)
        self.assertEqual(drug.get_update_url(), reverse('regimens_drug_update', kwargs={'pk':drug.pk}))

    def test_get_delete_url(self):
        """
        A method that tests the get_delete_url method of a model
        """
        drug = Drug.objects.get(id=1)
        self.assertEqual(drug.get_delete_url(), reverse('regimens_drug_delete', kwargs={'pk':drug.pk}))


class RegimenTestCase(TestCase):
    """
    Test cases for the Regimen model
    """
    def setUp(self):
        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE)
        Regimen.objects.create(patient=patient, notes='Sample notes', date_started=datetime.date.today())

    def test_str(self):
        """
        A test case for the __str__ method of the model
        """
        regimen = Regimen.objects.get(id=1)
        today = datetime.date.today()
        patient = regimen.patient
        self.assertEqual(regimen.__str__(), "{0}'s regimen that started on {1}".format(patient.get_full_name(), today))

        regimen.date_ended = today
        self.assertEqual(regimen.__str__(), "{0}'s regimen that started on {1} and ended on {2}".format(
            patient.get_full_name(), today, today))