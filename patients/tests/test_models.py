from django.test import TestCase
from django.core.urlresolvers import reverse

from patients.models import Patient, Enrollment
from programs.models import Program


class PatientTestCase(TestCase):
    """
    Test cases for the Patient model.
    """
    def setUp(self):
        Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE)

    def test_str(self):
        """
        A test case for the __str__ method for the Patient model.
        """
        patient = Patient.objects.get(id=1)
        self.assertEqual(patient.__str__(), 'Jon Snow')

        patient.identifier = 'A001'
        patient.save()
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


class EnrollmentTestCase(TestCase):
    """
    Test cases for the Enrollment model.
    """
    def setUp(self):
        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE)
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