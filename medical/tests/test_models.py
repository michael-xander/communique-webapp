from django.test import TestCase
from django.core.urlresolvers import reverse

from medical.models import MedicalReportType, MedicalReport
from patients.models import Patient


class MedicalReportTypeTestCase(TestCase):
    """
    Test cases for the medical report type model.
    """
    def setUp(self):
        MedicalReportType.objects.create(name='dummy type')

    def test_str(self):
        """
        Tests the __str__ method of the model
        """
        report_type = MedicalReportType.objects.get(id=1)
        self.assertEqual(report_type.__str__(), 'Dummy type')

    def test_get_absolute_url(self):
        """
        Tests the get_absolute_url method of the model
        """
        report_type = MedicalReportType.objects.get(id=1)
        self.assertEqual(report_type.get_absolute_url(), reverse('medical_report_type_detail',
                                                                 kwargs={'pk':report_type.pk}))

    def test_get_update_url(self):
        """
        Tests the get_update_url method of the model
        """
        report_type = MedicalReportType.objects.get(id=1)
        self.assertEqual(report_type.get_update_url(), reverse('medical_report_type_update',
                                                               kwargs={'pk':report_type.pk}))

    def test_get_delete_url(self):
        """
        Tests the get_delete_url method of the model
        """
        report_type = MedicalReportType.objects.get(id=1)
        self.assertEqual(report_type.get_delete_url(), reverse('medical_report_type_delete',
                                                               kwargs={'pk':report_type.pk}))


class MedicalReportTestCase(TestCase):
    """
    Test cases for the medical report model.
    """
    def setUp(self):
        report_type = MedicalReportType.objects.create(name='dummy type')
        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE)
        MedicalReport.objects.create(title='dummy report', report_type=report_type, patient=patient,
                                     notes='Sample notes')

    def test_str(self):
        """
        Tests the __str__ method of the model
        """
        medical_report = MedicalReport.objects.get(id=1)
        self.assertEqual(medical_report.__str__(), 'Dummy type report: Dummy report')

    def test_get_absolute_url(self):
        """
        Tests the get_absolute_url method of the model
        """
        medical_report = MedicalReport.objects.get(id=1)
        self.assertEqual(medical_report.get_absolute_url(), reverse('medical_report_detail',
                                                                    kwargs={'pk':medical_report.pk}))

    def test_get_update_url(self):
        """
        Tests the get_update_url method of the model
        """
        medical_report = MedicalReport.objects.get(id=1)
        self.assertEqual(medical_report.get_update_url(), reverse('medical_report_update',
                                                                  kwargs={'pk':medical_report.pk}))

    def test_get_delete_url(self):
        """
        Tests the get_delete_url method of the model
        """
        medical_report = MedicalReport.objects.get(id=1)
        self.assertEqual(medical_report.get_delete_url(), reverse('medical_report_delete',
                                                                  kwargs={'pk':medical_report.pk}))