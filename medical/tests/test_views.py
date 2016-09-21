from django.core.urlresolvers import reverse

from communique.utils import ViewsTestCase

from medical.models import MedicalReport, MedicalReportType
from patients.models import Patient


class MedicalReportTypeListViewTestCase(ViewsTestCase):
    """
    Test cases for the view that lists report types
    """
    view_name = 'medical_report_type_list'
    view_template_name = 'medical/medical_report_type_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class MedicalReportTypeCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create a new report type
    """
    view_name = 'medical_report_type_create'
    view_template_name = 'medical/medical_report_type_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingMedicalReportTypeViewTestCase(ViewsTestCase):
    """
    Test cases for a view that requires an existing medical report type for testing
    """
    def setUp(self):
        """
        Add medical report type to the test database
        """
        super(ExistingMedicalReportTypeViewTestCase, self).setUp()

        MedicalReportType.objects.create(name='dummy type')


class MedicalReportTypeDetailViewTestCase(ExistingMedicalReportTypeViewTestCase):
    """
    Test cases for the view to display details of a medical report type
    """
    view_template_name = 'medical/medical_report_type_view.html'

    def test_active_user_access(self):
        report_type = MedicalReportType.objects.get(id=1)
        self.only_active_user_access_test(report_type.get_absolute_url(), self.view_template_name)


class MedicalReportTypeUpdateViewTestCase(ExistingMedicalReportTypeViewTestCase):
    """
    Test cases for the view that handles updating a report type
    """
    view_template_name = 'medical/medical_report_type_update_form.html'

    def test_active_user_access(self):
        report_type = MedicalReportType.objects.get(id=1)
        self.only_active_user_access_test(report_type.get_update_url(), self.view_template_name)


class MedicalReportTypeDeleteViewTestCase(ExistingMedicalReportTypeViewTestCase):
    """
    Test cases for the view that handles deleting a report type
    """
    view_template_name = 'medical/medical_report_type_confirm_delete.html'

    def test_active_user_access(self):
        report_type = MedicalReportType.objects.get(id=1)
        self.only_active_user_access_test(report_type.get_delete_url(), self.view_template_name)


class MedicalReportCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create a medical report
    """
    view_name = 'medical_report_create'
    view_template_name = 'medical/medical_report_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class MedicalReportListViewTestCase(ViewsTestCase):
    """
    Test cases for the view to list medical reports
    """
    view_name = 'medical_report_list'
    view_template_name = 'medical/medical_report_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingMedicalReportViewTestCase(ViewsTestCase):
    """
    Test cases for a view that requires an existing medical report for testing
    """
    def setUp(self):
        """
        Add a medical report to the database
        """
        super(ExistingMedicalReportViewTestCase, self).setUp()
        report_type = MedicalReportType.objects.create(name='dummy type')
        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE)
        MedicalReport.objects.create(title='dummy report', patient=patient, report_type=report_type,
                                     notes='sample notes')


class MedicalReportDetailViewTestCase(ExistingMedicalReportViewTestCase):
    """
    Test cases for the view that displays a medical report's details
    """
    view_template_name = 'medical/medical_report_view.html'

    def test_active_user_access(self):
        report = MedicalReport.objects.get(id=1)
        self.only_active_user_access_test(report.get_absolute_url(), self.view_template_name)


class MedicalReportUpdateViewTestCase(ExistingMedicalReportViewTestCase):
    """
    Test cases for the view that handles updating a medical report
    """
    view_template_name = 'medical/medical_report_update_form.html'

    def test_active_user_access(self):
        report = MedicalReport.objects.get(id=1)
        self.only_active_user_access_test(report.get_update_url(), self.view_template_name)


class MedicalReportDeleteViewTestCase(ExistingMedicalReportViewTestCase):
    """
    Test cases for the view that handles medical report deletion
    """
    view_template_name = 'medical/medical_report_confirm_delete.html'

    def test_active_user_access(self):
        report = MedicalReport.objects.get(id=1)
        self.only_active_user_access_test(report.get_delete_url(), self.view_template_name)