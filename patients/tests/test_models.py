from django.test import TestCase
from django.core.urlresolvers import reverse

import datetime

from patients.models import Patient, Enrollment, Outcome, OutcomeType
from programs.models import Program


class PatientTestCase(TestCase):
    """
    Test cases for the Patient model.
    """
    def setUp(self):
        Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE, identifier='A001')

    def test_get_full_name(self):
        """
        A test case for the get_full_name method for the Patient model
        """
        patient = Patient.objects.get(id=1)
        self.assertEqual(patient.get_full_name(), 'Jon Snow')

    def test_str(self):
        """
        A test case for the __str__ method for the Patient model.
        """
        patient = Patient.objects.get(id=1)
        self.assertEqual(patient.__str__(), 'A001 - Jon Snow')

    def test_get_absolute_url(self):
        """
        A test case for the get_absolute_url method for the model.
        """
        patient = Patient.objects.get(id=1)
        self.assertEqual(patient.get_absolute_url(), reverse('patients_patient_detail', kwargs={'pk':patient.pk}))

    def test_get_update_url(self):
        """
        A test case for the get_update_url method for the model.
        """
        patient = Patient.objects.get(id=1)
        self.assertEqual(patient.get_update_url(), reverse('patients_patient_update', kwargs={'pk':patient.pk}))

    def test_get_delete_url(self):
        """
        A test case for the get_delete_url method for the model.
        """
        patient = Patient.objects.get(id=1)
        self.assertEqual(patient.get_delete_url(), reverse('patients_patient_delete', kwargs={'pk':patient.pk}))

    def test_get_contact_update_url(self):
        """
        A test case for the get_contact_update_url method for the model
        """
        patient = Patient.objects.get(id=1)
        self.assertEqual(patient.get_contact_update_url(), reverse('patients_patient_contact_update',
                                                                   kwargs={'pk':patient.pk}))

    def test_get_archive_url(self):
        """
        A test case for the get_archive_url method for the model
        """
        patient = Patient.objects.get(id=1)
        self.assertEqual(patient.get_archive_url(), reverse('patients_patient_archive', kwargs={'pk':patient.pk}))

    def test_get_unarchive_url(self):
        """
        A test case for the get_unarchive_url method for the model
        """
        patient = Patient.objects.get(id=1)
        self.assertEqual(patient.get_unarchive_url(), reverse('patients_patient_unarchive', kwargs={'pk':patient.pk}))


class EnrollmentTestCase(TestCase):
    """
    Test cases for the Enrollment model.
    """
    def setUp(self):
        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE, identifier='A001')
        program = Program.objects.create(name='Sample', description='Sample description')
        Enrollment.objects.create(patient=patient, program=program, comment='No comment')

    def test_str(self):
        """
        Test for the __str__  method of the model
        """
        enrollment = Enrollment.objects.get(id=1)
        self.assertEqual(enrollment.__str__(), 'Jon Snow into Sample')

    def test_get_absolute_url(self):
        """
        Tests the get_absolute_url method of the model
        """
        enrollment = Enrollment.objects.get(id=1)
        self.assertEqual(enrollment.get_absolute_url(), reverse('patients_enrollment_detail',
                                                                kwargs={'pk':enrollment.pk}))

    def test_get_update_url(self):
        """
        Tests the get_update_url method of the model
        """
        enrollment = Enrollment.objects.get(id=1)
        self.assertEqual(enrollment.get_update_url(), reverse('patients_enrollment_update',
                                                              kwargs={'pk':enrollment.pk}))


class OutcomeTypeTestCase(TestCase):
    """
    Test cases for the outcome type model
    """
    def setUp(self):
        self.outcome_type = OutcomeType.objects.create(name='Outcome type', description='Sample description')

    def test_str(self):
        """
        Test the __str__ method of the model
        """
        self.assertEqual(self.outcome_type.__str__(), self.outcome_type.name.title())

    def test_get_absolute_url(self):
        """
        Test the get_absolute_url method of the model
        """
        self.assertEqual(self.outcome_type.get_absolute_url(), reverse('patients_outcome_type_detail',
                                                                       kwargs={'pk':self.outcome_type.pk}))

    def test_get_update_url(self):
        """
        Test the get_update_url method of the model
        """
        self.assertEqual(self.outcome_type.get_update_url(), reverse('patients_outcome_type_update',
                                                                     kwargs={'pk':self.outcome_type.pk}))

    def test_get_delete_url(self):
        """
        Test the get_delete_url method of the model
        """
        self.assertEqual(self.outcome_type.get_delete_url(), reverse('patients_outcome_type_delete',
                                                                     kwargs={'pk':self.outcome_type.pk}))


class OutcomeTestCase(TestCase):
    """
    Test cases for the outcome model
    """
    def setUp(self):
        self.patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE, identifier='A001')
        self.outcome_type = OutcomeType.objects.create(name='Outcome type', description='Sample description')
        self.outcome = Outcome.objects.create(patient=self.patient, outcome_type=self.outcome_type,
                                              outcome_date=datetime.date.today())

    def test_str(self):
        """
        Test the __str__ method of the model
        """
        self.assertEqual(self.outcome.__str__(), "{0} outcome for {1} on {2}".format(self.outcome_type,
                                                                                     self.patient.get_full_name(),
                                                                                     self.outcome.outcome_date))

    def test_get_absolute_url(self):
        """
        Test the get_absolute_url method of the model
        """
        self.assertEqual(self.outcome.get_absolute_url(), reverse('patients_outcome_detail',
                                                                  kwargs={'pk':self.outcome.pk}))

    def test_get_update_url(self):
        """
        Test the get_update_url method of the model
        """
        self.assertEqual(self.outcome.get_update_url(), reverse('patients_outcome_update',
                                                                kwargs={'pk':self.outcome.pk}))
