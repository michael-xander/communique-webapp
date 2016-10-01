from django.core.urlresolvers import reverse

from communique.utils.utils_tests import ViewsTestCase

from patients.models import Patient, Enrollment
from programs.models import Program


class PatientListViewTestCase(ViewsTestCase):
    """
    Test cases for the view that lists patients.
    """
    view_name = 'patients_patient_list'
    view_template_name = 'patients/patient_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class PatientCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view that creates patients.
    """
    view_name = 'patients_patient_create'
    view_template_name = 'patients/patient_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class PatientImportViewTestCase(ViewsTestCase):
    """
    Test cases for the view that handles importation of patients.
    """
    view_name = 'patients_patient_import'
    view_template_name = 'patients/patient_import_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingPatientViewsTestCase(ViewsTestCase):
    """
    Test case for views that require an existing patient
    """
    def setUp(self):
        super(ExistingPatientViewsTestCase, self).setUp()
        Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE)


class PatientDetailViewTestCase(ExistingPatientViewsTestCase):
    """
    Test cases for the view that displays patient information.
    """
    view_template_name = 'patients/patient_view.html'

    def test_active_user_access(self):
        patient = Patient.objects.get(id=1)
        self.only_active_user_access_test(patient.get_absolute_url(), self.view_template_name)


class PatientUpdateViewTestCase(ExistingPatientViewsTestCase):
    """
    Test cases for the update view for patient information.
    """
    view_template_name = 'patients/patient_update_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.get(id=1)
        self.only_active_user_access_test(patient.get_update_url(), self.view_template_name)


class PatientContactUpdateViewTestCase(ExistingPatientViewsTestCase):
    """
    Test cases for the contact update view fora patient.
    """
    view_template_name = 'patients/patient_contact_update_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.get(id=1)
        self.only_active_user_access_test(patient.get_contact_update_url(), self.view_template_name)


class PatientDeleteViewTestCase(ExistingPatientViewsTestCase):
    """
    Test cases for the delete view of a patient.
    """
    view_template_name = 'patients/patient_confirm_delete.html'

    def test_active_user_access(self):
        patient = Patient.objects.get(id=1)
        self.only_active_user_access_test(patient.get_delete_url(), self.view_template_name)


class EnrollmentListViewTestCase(ViewsTestCase):
    """
    Test cases for the enrollment list view.
    """
    view_name = 'patients_enrollment_list'
    view_template_name = 'patients/enrollment_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class EnrollmentCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the enrollment create view.
    """
    view_name = 'patients_enrollment_create'
    view_template_name = 'patients/enrollment_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingEnrollmentViewsTestCase(ViewsTestCase):
    """
    Test case for views that require an existing enrollment
    """
    def setUp(self):
        super(ExistingEnrollmentViewsTestCase, self).setUp()
        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE)
        program = Program.objects.create(name='Sample', description='sample text')
        Enrollment.objects.create(patient=patient, program=program, comment='No comment')


class EnrollmentDetailViewTestCase(ExistingEnrollmentViewsTestCase):
    """
    Test cases for the enrollment detail view.
    """
    view_template_name = 'patients/enrollment_view.html'

    def test_active_user_access(self):
        enrollment = Enrollment.objects.get(id=1)
        self.only_active_user_access_test(enrollment.get_absolute_url(), self.view_template_name)


class EnrollmentUpdateViewTestCase(ExistingEnrollmentViewsTestCase):
    """
    Test cases for the enrollment update view.
    """
    view_template_name = 'patients/enrollment_update_form.html'

    def test_active_user_access(self):
        enrollment = Enrollment.objects.get(id=1)
        self.only_active_user_access_test(enrollment.get_update_url(), self.view_template_name)


class PatientEnrollmentCreateViewTestCase(ExistingPatientViewsTestCase):
    """
    Test cases for the view to create an enrollment for a specific patient.
    """
    view_name = 'patients_patient_enroll_create'
    view_template_name = 'patients/patient_enrollment_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.get(id=1)
        view_url = reverse(self.view_name, kwargs={'patient_pk':patient.pk})
        self.only_active_user_access_test(view_url, self.view_template_name)


class PatientSessionCreateViewTestCase(ExistingPatientViewsTestCase):
    """
    Test cases for the view to create a session for a specific patient.
    """
    view_name = 'patients_patient_session_create'
    view_template_name = 'patients/patient_session_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.get(id=1)
        view_url = reverse(self.view_name, kwargs={'patient_pk':patient.pk})
        self.only_active_user_access_test(view_url, self.view_template_name)


class PatientMedicalReportCreateViewTestCase(ExistingPatientViewsTestCase):
    """
    Test cases for the view to create a medical report for a specific patient.
    """
    view_name = 'patients_patient_medical_report_create'
    view_template_name = 'patients/patient_medical_report_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.get(id=1)
        view_url = reverse(self.view_name, kwargs={'patient_pk':patient.pk})
        self.only_active_user_access_test(view_url, self.view_template_name)


class PatientAppointmentCreateViewTestCase(ExistingPatientViewsTestCase):
    """
    Test cases for the view to create an appointment for a specific patient.
    """
    view_name = 'patients_patient_appointment_create'
    view_template_name = 'patients/patient_appointment_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.get(id=1)
        view_url = reverse(self.view_name, kwargs={'patient_pk':patient.pk})
        self.only_active_user_access_test(view_url, self.view_template_name)


class PatientAdmissionCreateViewTestCase(ExistingPatientViewsTestCase):
    """
    Test cases for the view to create an admission for a patient.
    """
    view_name = 'patients_patient_admission_create'
    view_template_name = 'patients/patient_admission_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.get(id=1)
        view_url = reverse(self.view_name, kwargs={'patient_pk':patient.pk})
        self.only_active_user_access_test(view_url, self.view_template_name)


class PatientAdverseEventCreateViewTestCase(ExistingPatientViewsTestCase):
    """
    Test cases for the view to report an adverse event for a patient.
    """
    view_name = 'patients_patient_adverse_event_create'
    view_template_name = 'patients/patient_adverse_event_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.get(id=1)
        view_url = reverse(self.view_name, kwargs={'patient_pk':patient.pk})
        self.only_active_user_access_test(view_url, self.view_template_name)