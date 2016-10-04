from django.core.urlresolvers import reverse

import datetime

from communique.utils.utils_tests import ViewsTestCase

from patients.models import Patient, Enrollment, Outcome, OutcomeType
from programs.models import Program


class PatientListViewTestCase(ViewsTestCase):
    """
    Test cases for the view that lists patients that are not archived.
    """
    view_name = 'patients_patient_list'
    view_template_name = 'patients/patient_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class PatientArchiveListViewTestCase(ViewsTestCase):
    """
    Test cases for the view that lists patients that are archived
    """
    view_name = 'patients_patient_archived_list'
    view_template_name = 'patients/patient_archived_list.html'
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
        Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE, identifier='A001')


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
    Test cases for the contact update view for a patient.
    """
    view_template_name = 'patients/patient_contact_update_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.get(id=1)
        self.only_active_user_access_test(patient.get_contact_update_url(), self.view_template_name)


class PatientArchiveViewTestCase(ExistingPatientViewsTestCase):
    """
    Test cases for the patient archive view
    """
    view_template_name = 'patients/patient_confirm_archive.html'

    def test_active_user_access(self):
        patient = Patient.objects.get(id=1)
        self.only_active_user_access_test(patient.get_archive_url(), self.view_template_name)


class PatientUnarchiveViewTestCase(ExistingPatientViewsTestCase):
    """
    Test cases for the patient unarchive view
    """
    view_template_name = 'patients/patient_confirm_unarchive.html'

    def test_active_user_access(self):
        patient = Patient.objects.get(id=1)
        self.only_active_user_access_test(patient.get_unarchive_url(), self.view_template_name)


class PatientDeleteViewTestCase(ExistingPatientViewsTestCase):
    """
    Test cases for the delete view of a patient.
    """
    view_template_name = 'patients/patient_confirm_delete.html'

    def test_active_user_access(self):
        patient = Patient.objects.get(id=1)
        self.only_active_user_access_test(patient.get_delete_url(), self.view_template_name)


class OutcomeTypeListViewTestCase(ViewsTestCase):
    """
    Test cases for the view to list outcome types
    """
    view_name = 'patients_outcome_type_list'
    view_template_name = 'patients/outcome_type_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class OutcomeTypeCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create an outcome type
    """
    view_name = 'patients_outcome_type_create'
    view_template_name = 'patients/outcome_type_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingOutcomeTypeViewsTestCase(ViewsTestCase):
    """
    Test cases for views that require an existing outcome type
    """
    def setUp(self):
        super(ExistingOutcomeTypeViewsTestCase, self).setUp()
        self.outcome_type = OutcomeType.objects.create(name='Outcome type', description='Sample description')


class OutcomeTypeDetailViewTestCase(ExistingOutcomeTypeViewsTestCase):
    """
    Test cases for the detail view of an outcome type
    """
    view_template_name = 'patients/outcome_type_view.html'

    def test_active_user_access(self):
        self.only_active_user_access_test(self.outcome_type.get_absolute_url(), self.view_template_name)


class OutcomeTypeUpdateViewTestCase(ExistingOutcomeTypeViewsTestCase):
    """
    Test cases for the update view of an outcome type
    """
    view_template_name = 'patients/outcome_type_update_form.html'

    def test_active_user_access(self):
        self.only_active_user_access_test(self.outcome_type.get_update_url(), self.view_template_name)


class OutcomeTypeDeleteViewTestCase(ExistingOutcomeTypeViewsTestCase):
    """
    Test cases for the view to delete an outcome type
    """
    view_template_name = 'patients/outcome_type_confirm_delete.html'

    def test_active_user_access(self):
        self.only_active_user_access_test(self.outcome_type.get_delete_url(), self.view_template_name)


class OutcomeListViewTestCase(ViewsTestCase):
    """
    Test cases for the view list outcomes
    """
    view_name = 'patients_outcome_list'
    view_template_name = 'patients/outcome_list.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class OutcomeCreateViewTestCase(ViewsTestCase):
    """
    Test cases for the view to create an outcome
    """
    view_name = 'patients_outcome_create'
    view_template_name = 'patients/outcome_form.html'
    view_url = reverse(view_name)

    def test_active_user_access(self):
        self.only_active_user_access_test(self.view_url, self.view_template_name)


class ExistingOutcomeViewsTestCase(ViewsTestCase):
    """
    Test cases for views that require an existing outcome
    """
    def setUp(self):
        super(ExistingOutcomeViewsTestCase, self).setUp()
        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE, identifier='A001')
        outcome_type = OutcomeType.objects.create(name='Outcome type', description='Sample description')
        self.outcome = Outcome.objects.create(patient=patient, outcome_type=outcome_type,
                                              outcome_date=datetime.date.today())


class OutcomeDetailViewTestCase(ExistingOutcomeViewsTestCase):
    """
    Test cases for the outcome detail view
    """
    view_template_name = 'patients/outcome_view.html'

    def test_active_user_access(self):
        self.only_active_user_access_test(self.outcome.get_absolute_url(), self.view_template_name)


class OutcomeUpdateViewTestCase(ExistingOutcomeViewsTestCase):
    """
    Test cases for the outcome update view
    """
    view_template_name = 'patients/outcome_update_form.html'

    def test_active_user_access(self):
        self.only_active_user_access_test(self.outcome.get_update_url(), self.view_template_name)


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
        patient = Patient.objects.create(other_names='Jon', last_name='Snow', sex=Patient.MALE, identifier='A001')
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


class PatientOutcomeCreateViewTestCase(ExistingPatientViewsTestCase):
    """
    Test cases for the view to add an outcome for a patient
    """
    view_name = 'patients_patient_outcome_create'
    view_template_name = 'patients/patient_outcome_form.html'

    def test_active_user_access(self):
        patient = Patient.objects.get(id=1)
        view_url = reverse(self.view_name, kwargs={'patient_pk':patient.pk})
        self.only_active_user_access_test(view_url, self.view_template_name)