from django.core.urlresolvers import reverse

import datetime

from communique.utils.utils_tests import ViewsTestCase
from admissions.models import Admission
from patients.models import Patient


class AdmissionCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create an admission.
    """
    view_name = 'admissions_admission_create'
    view_template_name = 'admissions/admission_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class AdmissionListViewTestCase(ViewsTestCase):
    """
    Test cases for the view to list admissions.
    """
    view_name = 'admissions_admission_list'
    view_template_name = 'admissions/admission_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingAdmissionViewTestCase(ViewsTestCase):
    """
    Test cases for a view that requires an existing admission for testing.
    """
    def setUp(self):
        """
        Add an admission to the test database
        """
        super(ExistingAdmissionViewTestCase, self).setUp()

        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE, identifier='A001')
        Admission.objects.create(patient=patient, admission_date=datetime.date.today(), health_centre="St.Michael's")


class AdmissionDetailViewTestCase(ExistingAdmissionViewTestCase):
    """
    Test cases for a view that displays an admission's information.
    """
    view_template_name = 'admissions/admission_view.html'

    def test_active_user_access(self):
        admission = Admission.objects.get(id=1)
        self.only_active_user_access_test(admission.get_absolute_url(), self.view_template_name)


class AdmissionUpdateViewTestCase(ExistingAdmissionViewTestCase):
    """
    Test cases for a view to update an admission.
    """
    view_template_name = 'admissions/admission_update_form.html'

    def test_active_user_access(self):
        admission = Admission.objects.get(id=1)
        self.only_active_user_access_test(admission.get_update_url(), self.view_template_name)


class AdmissionDeleteViewTestCase(ExistingAdmissionViewTestCase):
    """
    Test cases for a view to handle admission deletion.
    """
    view_template_name = 'admissions/admission_confirm_delete.html'

    def test_active_user_access(self):
        admission = Admission.objects.get(id=1)
        self.only_active_user_access_test(admission.get_delete_url(), self.view_template_name)